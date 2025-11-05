# Royalty-Free Sound Generator

A Python library for generating synthesized sound effects suitable for web and desktop applications. All sounds are procedurally generated and completely royalty-free.

## Features

Generate 48 different types of sounds across 14 categories:
- **Bells**: Simple bells, church bells, hand bells
- **Buzzers**: Error, warning, and success buzzer sounds
- **Doorbells**: Ding-dong, chime, and buzz styles
- **Notifications**: Message alerts, completion sounds, pops
- **UI Sounds**: Clicks, coins/pickup sounds
- **Cash Registers**: Classic, modern, cha-ching
- **Alarms**: Wake-up, timer, emergency
- **Phone Sounds**: Ringtone, busy signal, dial tone
- **Game Sounds**: Power-up, level-up, game over, jump, laser
- **Swoosh/Whoosh**: Transition sounds (short, medium, long)
- **System Beeps**: Info, warning, error, critical
- **Keyboard**: Mechanical, soft, typewriter
- **Camera**: Shutter sound
- **Lock/Unlock**: Security sounds
- **Clock**: Tick-tock
- **Bubbles**: Pop, small, large

All sounds are synthesized using harmonic frequencies and ADSR envelopes for natural-sounding audio.

## Pre-Generated Sounds

Don't want to run Python? All 48 sounds are included in the repository:
- **WAV format**: `generated_sounds/` directory (uncompressed, high quality)
- **MP3 format**: `generated_sounds_mp3/` directory (compressed, smaller files for web)

Download and use immediately in your projects!

## Requirements

```bash
pip install numpy
```

That's it! The library only uses Python's built-in `wave` module and numpy for audio generation.

## Quick Start

```python
from sound_generator import SoundGenerator

# Initialize the generator
generator = SoundGenerator(sample_rate=44100)

# Generate a simple bell sound
generator.generate_simple_bell("bell.wav")

# Generate a notification sound
generator.generate_notification("notify.wav", notification_type="message")

# Generate a doorbell
generator.generate_doorbell("doorbell.wav", style="ding-dong")
```

## Running Examples

Generate all available sound types:

```bash
python examples.py
```

This will create a `generated_sounds/` directory with 18 different sound files demonstrating all available sound types.

## API Reference

### SoundGenerator

#### `__init__(sample_rate=44100)`
Initialize the sound generator with specified sample rate.

#### Bell Sounds

**`generate_simple_bell(filename, base_frequency=800, duration=1.5)`**
- Creates a pleasant bell sound with harmonics
- `base_frequency`: Pitch of the bell in Hz (higher = brighter)
- `duration`: Length of sound in seconds

**`generate_church_bell(filename, base_frequency=200, duration=3.0)`**
- Deep, resonant church bell sound
- Lower frequencies for authentic church bell tone

**`generate_hand_bell(filename, base_frequency=1200, duration=0.8)`**
- Bright, crisp hand bell sound
- Higher frequencies for a clear ring

#### Buzzer Sounds

**`generate_buzzer(filename, frequency=400, duration=0.5, buzz_type="error")`**
- `buzz_type`: "error" (low/harsh), "warning" (medium), or "success" (high/clean)

#### Doorbell Sounds

**`generate_doorbell(filename, style="ding-dong")`**
- `style`:
  - "ding-dong": Classic two-tone doorbell
  - "chime": Pleasant multi-tone chime
  - "buzz": Electric buzzer doorbell

#### Notification Sounds

**`generate_notification(filename, notification_type="message")`**
- `notification_type`:
  - "message": Gentle ascending tones
  - "alert": Triple beep for attention
  - "complete": Success melody (ascending C-E-G)
  - "pop": Subtle single pop

#### UI Sounds

**`generate_coin(filename)`**
- Bright pickup/coin collection sound
- Quick ascending tones

**`generate_click(filename, click_type="soft")`**
- `click_type`: "soft", "hard", or "mechanical"

## Usage Examples

### Custom Bell Sound

```python
from sound_generator import SoundGenerator

generator = SoundGenerator()

# Create a high-pitched bell
generator.generate_simple_bell(
    "high_bell.wav",
    base_frequency=1200,  # Higher pitch
    duration=1.0          # Shorter duration
)

# Create a deep gong
generator.generate_church_bell(
    "gong.wav",
    base_frequency=150,   # Very low pitch
    duration=5.0          # Long resonance
)
```

### Notification System

```python
# Different notification types for your app
generator = SoundGenerator()

generator.generate_notification("new_message.wav", "message")
generator.generate_notification("task_done.wav", "complete")
generator.generate_notification("urgent.wav", "alert")
generator.generate_notification("subtle_pop.wav", "pop")
```

### UI Feedback Sounds

```python
# Button clicks
generator.generate_click("btn_soft.wav", "soft")
generator.generate_click("btn_hard.wav", "hard")

# Game sounds
generator.generate_coin("pickup.wav")
generator.generate_buzzer("level_complete.wav", buzz_type="success")
```

## Technical Details

### Sound Synthesis

All sounds are generated using:
- **Additive synthesis**: Multiple sine waves at harmonic frequencies
- **ADSR envelopes**: Attack, Decay, Sustain, Release for natural sound shaping
- **16-bit WAV format**: Standard audio format compatible with all platforms

### Customization

You can modify the `SoundGenerator` class to:
- Add new sound types
- Adjust harmonic ratios for different timbres
- Modify envelope parameters for different characteristics
- Change the sample rate for different quality/file size tradeoffs

## License

All generated sounds are completely royalty-free and can be used in any project (commercial or personal) without attribution. The sounds are synthesized, not sampled, so there are no copyright restrictions.

## Use Cases

- Web applications (notification sounds, UI feedback)
- Desktop applications (alerts, system sounds)
- Games (pickup sounds, UI elements, bells)
- Mobile apps (notifications, button clicks)
- Prototyping (quick placeholder sounds)
- Accessibility features (audio cues)

## Tips

1. **Frequency ranges**:
   - Sub-bass: 20-60 Hz (felt more than heard)
   - Bass: 60-250 Hz (deep sounds, gongs)
   - Midrange: 250-2000 Hz (most musical content)
   - Treble: 2000-6000 Hz (brightness, clarity)
   - High: 6000-20000 Hz (air, sparkle)

2. **Duration guidelines**:
   - UI clicks: 0.02-0.05 seconds
   - Notifications: 0.1-0.5 seconds
   - Bells: 0.8-3.0 seconds
   - Alerts: 0.3-1.0 seconds

3. **Volume levels**: All sounds are generated at moderate levels. You can adjust amplitude parameters in the code if needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

All generated sounds are completely royalty-free and can be used in any project (commercial or personal) without attribution.

## Contributing

Feel free to extend this library with additional sound types! The modular design makes it easy to add new synthesis methods and sound categories.
