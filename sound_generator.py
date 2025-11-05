"""
Royalty-Free Sound Generator
Generate various sound effects for web and desktop applications.
"""

import numpy as np
import wave
import struct
from typing import Tuple, Optional
from pathlib import Path


class SoundGenerator:
    """Generate various sound effects using synthesized audio."""

    def __init__(self, sample_rate: int = 44100):
        """
        Initialize the sound generator.

        Args:
            sample_rate: Audio sample rate in Hz (default: 44100)
        """
        self.sample_rate = sample_rate

    def _generate_sine_wave(self, frequency: float, duration: float,
                           amplitude: float = 0.5) -> np.ndarray:
        """Generate a sine wave."""
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        wave = amplitude * np.sin(2 * np.pi * frequency * t)
        return wave

    def _apply_envelope(self, audio: np.ndarray, attack: float = 0.01,
                       decay: float = 0.1, sustain: float = 0.7,
                       release: float = 0.2) -> np.ndarray:
        """Apply ADSR envelope to audio signal."""
        n_samples = len(audio)
        envelope = np.ones(n_samples)

        # Attack
        attack_samples = int(attack * self.sample_rate)
        if attack_samples > 0:
            envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

        # Decay
        decay_samples = int(decay * self.sample_rate)
        if decay_samples > 0:
            start = attack_samples
            end = start + decay_samples
            if end <= n_samples:
                envelope[start:end] = np.linspace(1, sustain, decay_samples)

        # Release
        release_samples = int(release * self.sample_rate)
        if release_samples > 0 and release_samples < n_samples:
            envelope[-release_samples:] = np.linspace(
                envelope[-release_samples], 0, release_samples
            )

        return audio * envelope

    def _save_wav(self, audio: np.ndarray, filename: str):
        """Save audio array to WAV file."""
        # Normalize to 16-bit range
        audio = np.clip(audio, -1.0, 1.0)
        audio_int16 = np.int16(audio * 32767)

        with wave.open(filename, 'w') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16-bit
            wav_file.setframerate(self.sample_rate)
            wav_file.writeframes(audio_int16.tobytes())

    def generate_simple_bell(self, filename: str = "simple_bell.wav",
                            base_frequency: float = 800,
                            duration: float = 1.5) -> str:
        """
        Generate a simple bell sound.

        Args:
            filename: Output filename
            base_frequency: Base frequency in Hz
            duration: Duration in seconds

        Returns:
            Path to generated file
        """
        # Bell sounds have multiple harmonic frequencies
        harmonics = [1, 2, 2.4, 3, 4.2]
        amplitudes = [1.0, 0.5, 0.3, 0.2, 0.15]

        audio = np.zeros(int(self.sample_rate * duration))

        for harmonic, amplitude in zip(harmonics, amplitudes):
            freq = base_frequency * harmonic
            wave = self._generate_sine_wave(freq, duration, amplitude * 0.3)
            audio += wave

        # Apply envelope with quick attack and slow decay
        audio = self._apply_envelope(audio, attack=0.001, decay=0.3,
                                     sustain=0.1, release=0.7)

        self._save_wav(audio, filename)
        return filename

    def generate_church_bell(self, filename: str = "church_bell.wav",
                            base_frequency: float = 200,
                            duration: float = 3.0) -> str:
        """
        Generate a deep church bell sound.

        Args:
            filename: Output filename
            base_frequency: Base frequency in Hz (lower for deeper sound)
            duration: Duration in seconds

        Returns:
            Path to generated file
        """
        # Church bells have complex harmonic structure
        harmonics = [1, 1.5, 2, 2.5, 3, 4, 5]
        amplitudes = [1.0, 0.6, 0.4, 0.3, 0.25, 0.15, 0.1]

        audio = np.zeros(int(self.sample_rate * duration))

        for harmonic, amplitude in zip(harmonics, amplitudes):
            freq = base_frequency * harmonic
            wave = self._generate_sine_wave(freq, duration, amplitude * 0.2)
            audio += wave

        # Long, slow decay
        audio = self._apply_envelope(audio, attack=0.001, decay=0.5,
                                     sustain=0.3, release=2.0)

        self._save_wav(audio, filename)
        return filename

    def generate_hand_bell(self, filename: str = "hand_bell.wav",
                          base_frequency: float = 1200,
                          duration: float = 0.8) -> str:
        """
        Generate a bright hand bell sound.

        Args:
            filename: Output filename
            base_frequency: Base frequency in Hz
            duration: Duration in seconds

        Returns:
            Path to generated file
        """
        harmonics = [1, 2, 3, 4.2, 5.4]
        amplitudes = [1.0, 0.4, 0.3, 0.15, 0.1]

        audio = np.zeros(int(self.sample_rate * duration))

        for harmonic, amplitude in zip(harmonics, amplitudes):
            freq = base_frequency * harmonic
            wave = self._generate_sine_wave(freq, duration, amplitude * 0.4)
            audio += wave

        audio = self._apply_envelope(audio, attack=0.001, decay=0.2,
                                     sustain=0.2, release=0.4)

        self._save_wav(audio, filename)
        return filename

    def generate_buzzer(self, filename: str = "buzzer.wav",
                       frequency: float = 400,
                       duration: float = 0.5,
                       buzz_type: str = "error") -> str:
        """
        Generate a buzzer sound.

        Args:
            filename: Output filename
            frequency: Base frequency in Hz
            duration: Duration in seconds
            buzz_type: Type of buzz - "error", "warning", or "success"

        Returns:
            Path to generated file
        """
        if buzz_type == "error":
            # Lower, harsh sound
            freq = 200
            harmonics = [1, 1.5, 2, 2.5]
            amplitudes = [1.0, 0.5, 0.3, 0.2]
        elif buzz_type == "warning":
            # Medium frequency
            freq = 400
            harmonics = [1, 2, 3]
            amplitudes = [1.0, 0.4, 0.2]
        else:  # success
            # Higher, cleaner sound
            freq = 600
            harmonics = [1, 2]
            amplitudes = [1.0, 0.3]

        audio = np.zeros(int(self.sample_rate * duration))

        for harmonic, amplitude in zip(harmonics, amplitudes):
            wave = self._generate_sine_wave(freq * harmonic, duration,
                                           amplitude * 0.5)
            audio += wave

        # Short, punchy envelope
        audio = self._apply_envelope(audio, attack=0.001, decay=0.05,
                                     sustain=0.8, release=0.1)

        self._save_wav(audio, filename)
        return filename

    def generate_doorbell(self, filename: str = "doorbell.wav",
                         style: str = "ding-dong") -> str:
        """
        Generate a doorbell sound.

        Args:
            filename: Output filename
            style: Doorbell style - "ding-dong", "chime", or "buzz"

        Returns:
            Path to generated file
        """
        if style == "ding-dong":
            # Classic two-tone doorbell
            duration1 = 0.3
            duration2 = 0.4

            # "Ding" - higher note
            audio1 = self._generate_sine_wave(800, duration1, 0.5)
            audio1 += self._generate_sine_wave(1600, duration1, 0.2)
            audio1 = self._apply_envelope(audio1, attack=0.001, decay=0.1,
                                         sustain=0.3, release=0.15)

            # Short pause
            pause = np.zeros(int(self.sample_rate * 0.1))

            # "Dong" - lower note
            audio2 = self._generate_sine_wave(600, duration2, 0.5)
            audio2 += self._generate_sine_wave(1200, duration2, 0.2)
            audio2 = self._apply_envelope(audio2, attack=0.001, decay=0.15,
                                         sustain=0.3, release=0.2)

            audio = np.concatenate([audio1, pause, audio2])

        elif style == "chime":
            # Pleasant multi-tone chime
            notes = [659, 784, 880]  # E, G, A
            segments = []

            for note in notes:
                segment = self._generate_sine_wave(note, 0.4, 0.3)
                segment += self._generate_sine_wave(note * 2, 0.4, 0.15)
                segment = self._apply_envelope(segment, attack=0.001, decay=0.1,
                                              sustain=0.4, release=0.3)
                segments.append(segment)
                segments.append(np.zeros(int(self.sample_rate * 0.05)))

            audio = np.concatenate(segments)

        else:  # buzz
            # Electric buzzer doorbell
            audio = self._generate_sine_wave(300, 0.8, 0.6)
            audio = self._apply_envelope(audio, attack=0.001, decay=0.05,
                                        sustain=0.9, release=0.05)

        self._save_wav(audio, filename)
        return filename

    def generate_notification(self, filename: str = "notification.wav",
                            notification_type: str = "message") -> str:
        """
        Generate a notification sound.

        Args:
            filename: Output filename
            notification_type: Type - "message", "alert", "complete", or "pop"

        Returns:
            Path to generated file
        """
        if notification_type == "message":
            # Gentle ascending tones
            freq1 = 600
            freq2 = 900

            tone1 = self._generate_sine_wave(freq1, 0.08, 0.4)
            tone1 = self._apply_envelope(tone1, attack=0.001, decay=0.03,
                                        sustain=0.5, release=0.04)

            tone2 = self._generate_sine_wave(freq2, 0.08, 0.4)
            tone2 = self._apply_envelope(tone2, attack=0.001, decay=0.03,
                                        sustain=0.5, release=0.04)

            audio = np.concatenate([tone1, tone2])

        elif notification_type == "alert":
            # Attention-grabbing triple beep
            beeps = []
            for _ in range(3):
                beep = self._generate_sine_wave(1000, 0.1, 0.5)
                beep = self._apply_envelope(beep, attack=0.001, decay=0.02,
                                           sustain=0.8, release=0.05)
                beeps.append(beep)
                beeps.append(np.zeros(int(self.sample_rate * 0.05)))

            audio = np.concatenate(beeps)

        elif notification_type == "complete":
            # Success sound - ascending notes
            notes = [523, 659, 784]  # C, E, G
            segments = []

            for note in notes:
                segment = self._generate_sine_wave(note, 0.1, 0.3)
                segment = self._apply_envelope(segment, attack=0.001, decay=0.03,
                                              sustain=0.5, release=0.05)
                segments.append(segment)

            audio = np.concatenate(segments)

        else:  # pop
            # Short, subtle pop sound
            audio = self._generate_sine_wave(800, 0.05, 0.4)
            audio += self._generate_sine_wave(1600, 0.05, 0.2)
            audio = self._apply_envelope(audio, attack=0.001, decay=0.01,
                                        sustain=0.3, release=0.03)

        self._save_wav(audio, filename)
        return filename

    def generate_coin(self, filename: str = "coin.wav") -> str:
        """
        Generate a coin/pickup sound effect.

        Args:
            filename: Output filename

        Returns:
            Path to generated file
        """
        # Bright, quick ascending tones
        freq1 = 988  # B
        freq2 = 1319  # E

        tone1 = self._generate_sine_wave(freq1, 0.08, 0.3)
        tone1 += self._generate_sine_wave(freq1 * 2, 0.08, 0.15)
        tone1 = self._apply_envelope(tone1, attack=0.001, decay=0.02,
                                    sustain=0.3, release=0.04)

        tone2 = self._generate_sine_wave(freq2, 0.1, 0.35)
        tone2 += self._generate_sine_wave(freq2 * 2, 0.1, 0.15)
        tone2 = self._apply_envelope(tone2, attack=0.001, decay=0.03,
                                    sustain=0.4, release=0.05)

        audio = np.concatenate([tone1, tone2])

        self._save_wav(audio, filename)
        return filename

    def generate_click(self, filename: str = "click.wav",
                      click_type: str = "soft") -> str:
        """
        Generate a click/button sound.

        Args:
            filename: Output filename
            click_type: Type - "soft", "hard", or "mechanical"

        Returns:
            Path to generated file
        """
        if click_type == "soft":
            duration = 0.03
            audio = self._generate_sine_wave(1000, duration, 0.3)
            audio += self._generate_sine_wave(2000, duration, 0.15)

        elif click_type == "hard":
            duration = 0.02
            audio = self._generate_sine_wave(1500, duration, 0.5)
            audio += self._generate_sine_wave(3000, duration, 0.2)

        else:  # mechanical
            duration = 0.04
            audio = self._generate_sine_wave(800, duration, 0.4)
            audio += self._generate_sine_wave(400, duration, 0.3)

        audio = self._apply_envelope(audio, attack=0.001, decay=0.005,
                                    sustain=0.2, release=0.01)

        self._save_wav(audio, filename)
        return filename

    def generate_cash_register(self, filename: str = "cash_register.wav",
                              register_type: str = "classic") -> str:
        """
        Generate a cash register sound.

        Args:
            filename: Output filename
            register_type: Type - "classic", "modern", or "cha-ching"

        Returns:
            Path to generated file
        """
        if register_type == "classic":
            # Classic mechanical register with bell at the end
            segments = []

            # Drawer opening sound - low mechanical rumble
            rumble_duration = 0.3
            rumble = self._generate_sine_wave(120, rumble_duration, 0.2)
            rumble += self._generate_sine_wave(180, rumble_duration, 0.15)
            rumble = self._apply_envelope(rumble, attack=0.01, decay=0.1,
                                         sustain=0.6, release=0.1)
            segments.append(rumble)

            # Brief pause
            segments.append(np.zeros(int(self.sample_rate * 0.05)))

            # Register bell "cha-ching"
            # "Cha" - metallic hit
            cha_duration = 0.15
            cha = self._generate_sine_wave(800, cha_duration, 0.4)
            cha += self._generate_sine_wave(1200, cha_duration, 0.3)
            cha += self._generate_sine_wave(1600, cha_duration, 0.2)
            cha = self._apply_envelope(cha, attack=0.001, decay=0.05,
                                      sustain=0.3, release=0.08)
            segments.append(cha)

            # "Ching" - bell ring
            ching_duration = 0.5
            ching = self._generate_sine_wave(1200, ching_duration, 0.5)
            ching += self._generate_sine_wave(2400, ching_duration, 0.3)
            ching += self._generate_sine_wave(3600, ching_duration, 0.2)
            ching = self._apply_envelope(ching, attack=0.001, decay=0.2,
                                        sustain=0.2, release=0.3)
            segments.append(ching)

            audio = np.concatenate(segments)

        elif register_type == "modern":
            # Modern electronic register beep
            segments = []

            # Quick beep
            beep = self._generate_sine_wave(1000, 0.1, 0.4)
            beep = self._apply_envelope(beep, attack=0.001, decay=0.02,
                                       sustain=0.7, release=0.05)
            segments.append(beep)

            # Short pause
            segments.append(np.zeros(int(self.sample_rate * 0.05)))

            # Confirmation tone - ascending notes
            note1 = self._generate_sine_wave(800, 0.08, 0.3)
            note1 = self._apply_envelope(note1, attack=0.001, decay=0.02,
                                        sustain=0.5, release=0.04)
            segments.append(note1)

            note2 = self._generate_sine_wave(1200, 0.1, 0.35)
            note2 = self._apply_envelope(note2, attack=0.001, decay=0.03,
                                        sustain=0.5, release=0.05)
            segments.append(note2)

            audio = np.concatenate(segments)

        else:  # cha-ching
            # Classic "cha-ching" bell sound only
            segments = []

            # "Cha" - quick metallic percussion
            cha_duration = 0.1
            cha = self._generate_sine_wave(900, cha_duration, 0.45)
            cha += self._generate_sine_wave(1350, cha_duration, 0.35)
            cha += self._generate_sine_wave(1800, cha_duration, 0.25)
            cha = self._apply_envelope(cha, attack=0.001, decay=0.03,
                                      sustain=0.4, release=0.06)
            segments.append(cha)

            # Very brief pause
            segments.append(np.zeros(int(self.sample_rate * 0.02)))

            # "Ching" - resonant bell
            ching_duration = 0.6
            ching = self._generate_sine_wave(1400, ching_duration, 0.5)
            ching += self._generate_sine_wave(2800, ching_duration, 0.35)
            ching += self._generate_sine_wave(4200, ching_duration, 0.2)
            ching += self._generate_sine_wave(5600, ching_duration, 0.1)
            ching = self._apply_envelope(ching, attack=0.001, decay=0.25,
                                        sustain=0.15, release=0.35)
            segments.append(ching)

            audio = np.concatenate(segments)

        self._save_wav(audio, filename)
        return filename

    def generate_alarm(self, filename: str = "alarm.wav",
                      alarm_type: str = "wake-up") -> str:
        """
        Generate an alarm sound.

        Args:
            filename: Output filename
            alarm_type: Type - "wake-up", "timer", or "emergency"

        Returns:
            Path to generated file
        """
        if alarm_type == "wake-up":
            # Gentle escalating alarm
            segments = []

            # Gradual beeping with increasing intensity
            for i in range(4):
                beep_duration = 0.3
                amplitude = 0.2 + (i * 0.1)

                beep = self._generate_sine_wave(800, beep_duration, amplitude)
                beep += self._generate_sine_wave(1600, beep_duration, amplitude * 0.5)
                beep = self._apply_envelope(beep, attack=0.01, decay=0.1,
                                           sustain=0.7, release=0.1)
                segments.append(beep)

                # Pause between beeps (decreasing)
                pause_duration = 0.5 - (i * 0.1)
                segments.append(np.zeros(int(self.sample_rate * pause_duration)))

            audio = np.concatenate(segments)

        elif alarm_type == "timer":
            # Simple repeating beep
            segments = []

            for _ in range(3):
                beep = self._generate_sine_wave(1000, 0.2, 0.4)
                beep = self._apply_envelope(beep, attack=0.01, decay=0.05,
                                           sustain=0.8, release=0.05)
                segments.append(beep)
                segments.append(np.zeros(int(self.sample_rate * 0.2)))

            audio = np.concatenate(segments)

        else:  # emergency
            # Urgent alternating tones (siren-like)
            segments = []

            for i in range(6):
                freq = 800 if i % 2 == 0 else 600
                tone = self._generate_sine_wave(freq, 0.25, 0.5)
                tone = self._apply_envelope(tone, attack=0.01, decay=0.05,
                                           sustain=0.9, release=0.02)
                segments.append(tone)

            audio = np.concatenate(segments)

        self._save_wav(audio, filename)
        return filename

    def generate_phone(self, filename: str = "phone.wav",
                      phone_type: str = "ringtone") -> str:
        """
        Generate phone sounds.

        Args:
            filename: Output filename
            phone_type: Type - "ringtone", "busy", or "dial-tone"

        Returns:
            Path to generated file
        """
        if phone_type == "ringtone":
            # Classic phone ring - two bursts
            segments = []

            for _ in range(2):
                # Ring burst
                ring_duration = 0.4
                ring = self._generate_sine_wave(440, ring_duration, 0.4)
                ring += self._generate_sine_wave(880, ring_duration, 0.3)

                # Vibrato effect
                t = np.linspace(0, ring_duration, int(self.sample_rate * ring_duration), False)
                vibrato = 1 + 0.1 * np.sin(2 * np.pi * 20 * t)
                ring = ring * vibrato

                ring = self._apply_envelope(ring, attack=0.01, decay=0.1,
                                           sustain=0.8, release=0.1)
                segments.append(ring)
                segments.append(np.zeros(int(self.sample_rate * 0.2)))

            # Pause before next ring cycle
            segments.append(np.zeros(int(self.sample_rate * 1.0)))

            audio = np.concatenate(segments)

        elif phone_type == "busy":
            # Busy signal - alternating on/off
            segments = []

            for _ in range(4):
                tone = self._generate_sine_wave(480, 0.25, 0.4)
                tone += self._generate_sine_wave(620, 0.25, 0.4)
                segments.append(tone)
                segments.append(np.zeros(int(self.sample_rate * 0.25)))

            audio = np.concatenate(segments)

        else:  # dial-tone
            # Continuous dual tone
            duration = 2.0
            audio = self._generate_sine_wave(350, duration, 0.3)
            audio += self._generate_sine_wave(440, duration, 0.3)

        self._save_wav(audio, filename)
        return filename

    def generate_game_sound(self, filename: str = "game.wav",
                           game_type: str = "power-up") -> str:
        """
        Generate game sound effects.

        Args:
            filename: Output filename
            game_type: Type - "power-up", "level-up", "game-over", "jump", or "laser"

        Returns:
            Path to generated file
        """
        if game_type == "power-up":
            # Ascending arpeggio
            notes = [262, 330, 392, 523]  # C, E, G, C
            segments = []

            for note in notes:
                tone = self._generate_sine_wave(note, 0.08, 0.3)
                tone += self._generate_sine_wave(note * 2, 0.08, 0.15)
                tone = self._apply_envelope(tone, attack=0.001, decay=0.02,
                                           sustain=0.5, release=0.03)
                segments.append(tone)

            audio = np.concatenate(segments)

        elif game_type == "level-up":
            # Triumphant fanfare
            notes = [523, 659, 784, 1047]  # C, E, G, C (higher octave)
            segments = []

            for i, note in enumerate(notes):
                duration = 0.15 if i < 3 else 0.3
                tone = self._generate_sine_wave(note, duration, 0.35)
                tone += self._generate_sine_wave(note * 2, duration, 0.2)
                tone = self._apply_envelope(tone, attack=0.001, decay=0.05,
                                           sustain=0.7, release=0.1)
                segments.append(tone)

            audio = np.concatenate(segments)

        elif game_type == "game-over":
            # Descending sad melody
            notes = [392, 349, 330, 262]  # G, F, E, C
            segments = []

            for note in notes:
                tone = self._generate_sine_wave(note, 0.3, 0.3)
                tone = self._apply_envelope(tone, attack=0.01, decay=0.1,
                                           sustain=0.7, release=0.15)
                segments.append(tone)

            audio = np.concatenate(segments)

        elif game_type == "jump":
            # Quick rising pitch
            duration = 0.15
            t = np.linspace(0, duration, int(self.sample_rate * duration), False)

            # Frequency sweep from 200 to 600 Hz
            freq_sweep = 200 + 400 * t / duration
            phase = 2 * np.pi * np.cumsum(freq_sweep) / self.sample_rate
            audio = 0.3 * np.sin(phase)

            audio = self._apply_envelope(audio, attack=0.001, decay=0.05,
                                        sustain=0.3, release=0.08)

        else:  # laser
            # Quick descending pitch with harmonics
            duration = 0.2
            t = np.linspace(0, duration, int(self.sample_rate * duration), False)

            # Frequency sweep from 1200 to 300 Hz
            freq_sweep = 1200 - 900 * t / duration
            phase = 2 * np.pi * np.cumsum(freq_sweep) / self.sample_rate
            audio = 0.4 * np.sin(phase)

            # Add harmonic
            freq_sweep2 = 2400 - 1800 * t / duration
            phase2 = 2 * np.pi * np.cumsum(freq_sweep2) / self.sample_rate
            audio += 0.2 * np.sin(phase2)

            audio = self._apply_envelope(audio, attack=0.001, decay=0.05,
                                        sustain=0.4, release=0.12)

        self._save_wav(audio, filename)
        return filename

    def generate_swoosh(self, filename: str = "swoosh.wav",
                       swoosh_type: str = "medium") -> str:
        """
        Generate swoosh/whoosh transition sounds.

        Args:
            filename: Output filename
            swoosh_type: Type - "short", "medium", or "long"

        Returns:
            Path to generated file
        """
        if swoosh_type == "short":
            duration = 0.15
        elif swoosh_type == "medium":
            duration = 0.3
        else:  # long
            duration = 0.5

        t = np.linspace(0, duration, int(self.sample_rate * duration), False)

        # Frequency sweep from high to low (whoosh effect)
        freq_sweep = 2000 - 1500 * t / duration
        phase = 2 * np.pi * np.cumsum(freq_sweep) / self.sample_rate

        # Create noise-like quality with multiple harmonics
        audio = 0.2 * np.sin(phase)
        audio += 0.15 * np.sin(phase * 1.5)
        audio += 0.1 * np.sin(phase * 2.3)

        # Add some noise
        noise = np.random.uniform(-0.05, 0.05, len(audio))
        audio += noise

        # Smooth envelope
        audio = self._apply_envelope(audio, attack=0.01, decay=0.1,
                                    sustain=0.5, release=0.2)

        self._save_wav(audio, filename)
        return filename

    def generate_system_beep(self, filename: str = "system_beep.wav",
                            beep_type: str = "info") -> str:
        """
        Generate system error/warning beeps.

        Args:
            filename: Output filename
            beep_type: Type - "info", "warning", "error", or "critical"

        Returns:
            Path to generated file
        """
        if beep_type == "info":
            # Single pleasant beep
            audio = self._generate_sine_wave(800, 0.1, 0.3)
            audio = self._apply_envelope(audio, attack=0.001, decay=0.03,
                                        sustain=0.6, release=0.05)

        elif beep_type == "warning":
            # Double beep
            beep1 = self._generate_sine_wave(600, 0.08, 0.35)
            beep1 = self._apply_envelope(beep1, attack=0.001, decay=0.02,
                                        sustain=0.7, release=0.04)

            pause = np.zeros(int(self.sample_rate * 0.05))

            beep2 = self._generate_sine_wave(600, 0.08, 0.35)
            beep2 = self._apply_envelope(beep2, attack=0.001, decay=0.02,
                                        sustain=0.7, release=0.04)

            audio = np.concatenate([beep1, pause, beep2])

        elif beep_type == "error":
            # Low harsh beep
            audio = self._generate_sine_wave(300, 0.3, 0.4)
            audio += self._generate_sine_wave(450, 0.3, 0.3)
            audio = self._apply_envelope(audio, attack=0.01, decay=0.05,
                                        sustain=0.8, release=0.1)

        else:  # critical
            # Urgent repeated beeps
            segments = []
            for _ in range(3):
                beep = self._generate_sine_wave(400, 0.1, 0.45)
                beep = self._apply_envelope(beep, attack=0.001, decay=0.02,
                                           sustain=0.8, release=0.03)
                segments.append(beep)
                segments.append(np.zeros(int(self.sample_rate * 0.05)))

            audio = np.concatenate(segments)

        self._save_wav(audio, filename)
        return filename

    def generate_keyboard(self, filename: str = "keyboard.wav",
                         key_type: str = "mechanical") -> str:
        """
        Generate keyboard/typing sounds.

        Args:
            filename: Output filename
            key_type: Type - "mechanical", "soft", or "typewriter"

        Returns:
            Path to generated file
        """
        if key_type == "mechanical":
            # Sharp click with resonance
            duration = 0.03
            audio = self._generate_sine_wave(1500, duration, 0.3)
            audio += self._generate_sine_wave(3000, duration, 0.2)
            audio += self._generate_sine_wave(4500, duration, 0.1)

            # Add noise for texture
            noise = np.random.uniform(-0.05, 0.05, len(audio))
            audio += noise

            audio = self._apply_envelope(audio, attack=0.001, decay=0.01,
                                        sustain=0.2, release=0.015)

        elif key_type == "soft":
            # Gentle tap
            duration = 0.02
            audio = self._generate_sine_wave(800, duration, 0.2)
            audio += self._generate_sine_wave(1600, duration, 0.1)
            audio = self._apply_envelope(audio, attack=0.001, decay=0.005,
                                        sustain=0.3, release=0.01)

        else:  # typewriter
            # Classic typewriter clack
            duration = 0.04

            # Initial impact
            impact = self._generate_sine_wave(1200, 0.01, 0.4)
            impact += self._generate_sine_wave(2400, 0.01, 0.2)

            # Resonance
            resonance = self._generate_sine_wave(800, 0.03, 0.15)
            resonance = self._apply_envelope(resonance, attack=0.001, decay=0.01,
                                            sustain=0.3, release=0.015)

            audio = np.concatenate([impact, resonance])

        self._save_wav(audio, filename)
        return filename

    def generate_camera_shutter(self, filename: str = "camera_shutter.wav") -> str:
        """
        Generate a camera shutter sound.

        Args:
            filename: Output filename

        Returns:
            Path to generated file
        """
        segments = []

        # Shutter opening - quick mechanical sound
        open_sound = self._generate_sine_wave(800, 0.03, 0.3)
        open_sound += self._generate_sine_wave(1200, 0.03, 0.2)

        # Add noise for mechanical texture
        noise1 = np.random.uniform(-0.1, 0.1, len(open_sound))
        open_sound += noise1

        open_sound = self._apply_envelope(open_sound, attack=0.001, decay=0.01,
                                         sustain=0.3, release=0.015)
        segments.append(open_sound)

        # Very brief pause
        segments.append(np.zeros(int(self.sample_rate * 0.02)))

        # Shutter closing
        close_sound = self._generate_sine_wave(700, 0.025, 0.25)
        close_sound += self._generate_sine_wave(1100, 0.025, 0.15)

        noise2 = np.random.uniform(-0.08, 0.08, len(close_sound))
        close_sound += noise2

        close_sound = self._apply_envelope(close_sound, attack=0.001, decay=0.008,
                                          sustain=0.2, release=0.012)
        segments.append(close_sound)

        audio = np.concatenate(segments)

        self._save_wav(audio, filename)
        return filename

    def generate_lock(self, filename: str = "lock.wav",
                     lock_type: str = "unlock") -> str:
        """
        Generate lock/unlock sounds.

        Args:
            filename: Output filename
            lock_type: Type - "lock" or "unlock"

        Returns:
            Path to generated file
        """
        segments = []

        if lock_type == "lock":
            # Descending pitch - closing/locking
            click = self._generate_sine_wave(1000, 0.05, 0.3)
            click += self._generate_sine_wave(500, 0.05, 0.2)
            click = self._apply_envelope(click, attack=0.001, decay=0.015,
                                        sustain=0.3, release=0.025)
            segments.append(click)

            # Mechanical settling
            settle = self._generate_sine_wave(300, 0.08, 0.15)
            settle = self._apply_envelope(settle, attack=0.01, decay=0.03,
                                         sustain=0.4, release=0.03)
            segments.append(settle)

        else:  # unlock
            # Ascending pitch - opening/unlocking
            click = self._generate_sine_wave(500, 0.05, 0.3)
            click += self._generate_sine_wave(1000, 0.05, 0.25)
            click = self._apply_envelope(click, attack=0.001, decay=0.015,
                                        sustain=0.3, release=0.025)
            segments.append(click)

            # Release sound
            release = self._generate_sine_wave(1200, 0.06, 0.2)
            release = self._apply_envelope(release, attack=0.005, decay=0.02,
                                          sustain=0.3, release=0.03)
            segments.append(release)

        audio = np.concatenate(segments)

        self._save_wav(audio, filename)
        return filename

    def generate_tick_tock(self, filename: str = "tick_tock.wav",
                          cycles: int = 3) -> str:
        """
        Generate tick-tock clock sound.

        Args:
            filename: Output filename
            cycles: Number of tick-tock cycles

        Returns:
            Path to generated file
        """
        segments = []

        for _ in range(cycles):
            # Tick - higher pitch
            tick = self._generate_sine_wave(1200, 0.02, 0.25)
            tick += self._generate_sine_wave(2400, 0.02, 0.12)
            tick = self._apply_envelope(tick, attack=0.001, decay=0.005,
                                       sustain=0.2, release=0.01)
            segments.append(tick)

            # Pause
            segments.append(np.zeros(int(self.sample_rate * 0.48)))

            # Tock - lower pitch
            tock = self._generate_sine_wave(1000, 0.02, 0.25)
            tock += self._generate_sine_wave(2000, 0.02, 0.12)
            tock = self._apply_envelope(tock, attack=0.001, decay=0.005,
                                       sustain=0.2, release=0.01)
            segments.append(tock)

            # Pause
            segments.append(np.zeros(int(self.sample_rate * 0.48)))

        audio = np.concatenate(segments)

        self._save_wav(audio, filename)
        return filename

    def generate_bubble(self, filename: str = "bubble.wav",
                       bubble_type: str = "pop") -> str:
        """
        Generate bubble/pop sounds.

        Args:
            filename: Output filename
            bubble_type: Type - "pop", "small", or "large"

        Returns:
            Path to generated file
        """
        if bubble_type == "pop":
            # Quick high-pitched pop
            duration = 0.08
            t = np.linspace(0, duration, int(self.sample_rate * duration), False)

            # Quick frequency drop
            freq_sweep = 1500 - 1200 * t / duration
            phase = 2 * np.pi * np.cumsum(freq_sweep) / self.sample_rate
            audio = 0.3 * np.sin(phase)

            audio = self._apply_envelope(audio, attack=0.001, decay=0.02,
                                        sustain=0.1, release=0.05)

        elif bubble_type == "small":
            # Tiny bubble sound
            audio = self._generate_sine_wave(2000, 0.05, 0.2)
            audio += self._generate_sine_wave(3000, 0.05, 0.1)
            audio = self._apply_envelope(audio, attack=0.001, decay=0.01,
                                        sustain=0.2, release=0.03)

        else:  # large
            # Bigger, deeper bubble
            duration = 0.12
            t = np.linspace(0, duration, int(self.sample_rate * duration), False)

            freq_sweep = 800 - 400 * t / duration
            phase = 2 * np.pi * np.cumsum(freq_sweep) / self.sample_rate
            audio = 0.35 * np.sin(phase)
            audio += 0.15 * np.sin(phase * 2)

            audio = self._apply_envelope(audio, attack=0.001, decay=0.03,
                                        sustain=0.2, release=0.08)

        self._save_wav(audio, filename)
        return filename
