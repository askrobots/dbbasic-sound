#!/usr/bin/env python3
"""
Example usage of the Sound Generator library.
Run this script to generate sample sounds of each type.
"""

from sound_generator import SoundGenerator
from pathlib import Path


def main():
    """Generate examples of all sound types."""
    print("Royalty-Free Sound Generator - Examples")
    print("=" * 50)

    # Create output directory
    output_dir = Path("generated_sounds")
    output_dir.mkdir(exist_ok=True)
    print(f"\nGenerating sounds in: {output_dir}/\n")

    # Initialize generator
    generator = SoundGenerator(sample_rate=44100)

    # Bell sounds
    print("Generating bell sounds...")
    generator.generate_simple_bell(
        f"{output_dir}/simple_bell.wav",
        base_frequency=800,
        duration=1.5
    )
    print("  ✓ simple_bell.wav")

    generator.generate_church_bell(
        f"{output_dir}/church_bell.wav",
        base_frequency=200,
        duration=3.0
    )
    print("  ✓ church_bell.wav")

    generator.generate_hand_bell(
        f"{output_dir}/hand_bell.wav",
        base_frequency=1200,
        duration=0.8
    )
    print("  ✓ hand_bell.wav")

    # Buzzer sounds
    print("\nGenerating buzzer sounds...")
    generator.generate_buzzer(
        f"{output_dir}/buzzer_error.wav",
        buzz_type="error"
    )
    print("  ✓ buzzer_error.wav")

    generator.generate_buzzer(
        f"{output_dir}/buzzer_warning.wav",
        buzz_type="warning"
    )
    print("  ✓ buzzer_warning.wav")

    generator.generate_buzzer(
        f"{output_dir}/buzzer_success.wav",
        buzz_type="success"
    )
    print("  ✓ buzzer_success.wav")

    # Doorbell sounds
    print("\nGenerating doorbell sounds...")
    generator.generate_doorbell(
        f"{output_dir}/doorbell_ding_dong.wav",
        style="ding-dong"
    )
    print("  ✓ doorbell_ding_dong.wav")

    generator.generate_doorbell(
        f"{output_dir}/doorbell_chime.wav",
        style="chime"
    )
    print("  ✓ doorbell_chime.wav")

    generator.generate_doorbell(
        f"{output_dir}/doorbell_buzz.wav",
        style="buzz"
    )
    print("  ✓ doorbell_buzz.wav")

    # Notification sounds
    print("\nGenerating notification sounds...")
    generator.generate_notification(
        f"{output_dir}/notification_message.wav",
        notification_type="message"
    )
    print("  ✓ notification_message.wav")

    generator.generate_notification(
        f"{output_dir}/notification_alert.wav",
        notification_type="alert"
    )
    print("  ✓ notification_alert.wav")

    generator.generate_notification(
        f"{output_dir}/notification_complete.wav",
        notification_type="complete"
    )
    print("  ✓ notification_complete.wav")

    generator.generate_notification(
        f"{output_dir}/notification_pop.wav",
        notification_type="pop"
    )
    print("  ✓ notification_pop.wav")

    # UI sounds
    print("\nGenerating UI sounds...")
    generator.generate_coin(f"{output_dir}/coin.wav")
    print("  ✓ coin.wav")

    generator.generate_click(
        f"{output_dir}/click_soft.wav",
        click_type="soft"
    )
    print("  ✓ click_soft.wav")

    generator.generate_click(
        f"{output_dir}/click_hard.wav",
        click_type="hard"
    )
    print("  ✓ click_hard.wav")

    generator.generate_click(
        f"{output_dir}/click_mechanical.wav",
        click_type="mechanical"
    )
    print("  ✓ click_mechanical.wav")

    # Cash register sounds
    print("\nGenerating cash register sounds...")
    generator.generate_cash_register(
        f"{output_dir}/cash_register_classic.wav",
        register_type="classic"
    )
    print("  ✓ cash_register_classic.wav")

    generator.generate_cash_register(
        f"{output_dir}/cash_register_modern.wav",
        register_type="modern"
    )
    print("  ✓ cash_register_modern.wav")

    generator.generate_cash_register(
        f"{output_dir}/cash_register_cha_ching.wav",
        register_type="cha-ching"
    )
    print("  ✓ cash_register_cha_ching.wav")

    # Alarm sounds
    print("\nGenerating alarm sounds...")
    generator.generate_alarm(
        f"{output_dir}/alarm_wake_up.wav",
        alarm_type="wake-up"
    )
    print("  ✓ alarm_wake_up.wav")

    generator.generate_alarm(
        f"{output_dir}/alarm_timer.wav",
        alarm_type="timer"
    )
    print("  ✓ alarm_timer.wav")

    generator.generate_alarm(
        f"{output_dir}/alarm_emergency.wav",
        alarm_type="emergency"
    )
    print("  ✓ alarm_emergency.wav")

    # Phone sounds
    print("\nGenerating phone sounds...")
    generator.generate_phone(
        f"{output_dir}/phone_ringtone.wav",
        phone_type="ringtone"
    )
    print("  ✓ phone_ringtone.wav")

    generator.generate_phone(
        f"{output_dir}/phone_busy.wav",
        phone_type="busy"
    )
    print("  ✓ phone_busy.wav")

    generator.generate_phone(
        f"{output_dir}/phone_dial_tone.wav",
        phone_type="dial-tone"
    )
    print("  ✓ phone_dial_tone.wav")

    # Game sounds
    print("\nGenerating game sounds...")
    generator.generate_game_sound(
        f"{output_dir}/game_power_up.wav",
        game_type="power-up"
    )
    print("  ✓ game_power_up.wav")

    generator.generate_game_sound(
        f"{output_dir}/game_level_up.wav",
        game_type="level-up"
    )
    print("  ✓ game_level_up.wav")

    generator.generate_game_sound(
        f"{output_dir}/game_over.wav",
        game_type="game-over"
    )
    print("  ✓ game_over.wav")

    generator.generate_game_sound(
        f"{output_dir}/game_jump.wav",
        game_type="jump"
    )
    print("  ✓ game_jump.wav")

    generator.generate_game_sound(
        f"{output_dir}/game_laser.wav",
        game_type="laser"
    )
    print("  ✓ game_laser.wav")

    # Swoosh sounds
    print("\nGenerating swoosh sounds...")
    generator.generate_swoosh(
        f"{output_dir}/swoosh_short.wav",
        swoosh_type="short"
    )
    print("  ✓ swoosh_short.wav")

    generator.generate_swoosh(
        f"{output_dir}/swoosh_medium.wav",
        swoosh_type="medium"
    )
    print("  ✓ swoosh_medium.wav")

    generator.generate_swoosh(
        f"{output_dir}/swoosh_long.wav",
        swoosh_type="long"
    )
    print("  ✓ swoosh_long.wav")

    # System beep sounds
    print("\nGenerating system beep sounds...")
    generator.generate_system_beep(
        f"{output_dir}/system_beep_info.wav",
        beep_type="info"
    )
    print("  ✓ system_beep_info.wav")

    generator.generate_system_beep(
        f"{output_dir}/system_beep_warning.wav",
        beep_type="warning"
    )
    print("  ✓ system_beep_warning.wav")

    generator.generate_system_beep(
        f"{output_dir}/system_beep_error.wav",
        beep_type="error"
    )
    print("  ✓ system_beep_error.wav")

    generator.generate_system_beep(
        f"{output_dir}/system_beep_critical.wav",
        beep_type="critical"
    )
    print("  ✓ system_beep_critical.wav")

    # Keyboard sounds
    print("\nGenerating keyboard sounds...")
    generator.generate_keyboard(
        f"{output_dir}/keyboard_mechanical.wav",
        key_type="mechanical"
    )
    print("  ✓ keyboard_mechanical.wav")

    generator.generate_keyboard(
        f"{output_dir}/keyboard_soft.wav",
        key_type="soft"
    )
    print("  ✓ keyboard_soft.wav")

    generator.generate_keyboard(
        f"{output_dir}/keyboard_typewriter.wav",
        key_type="typewriter"
    )
    print("  ✓ keyboard_typewriter.wav")

    # Camera shutter
    print("\nGenerating camera shutter sound...")
    generator.generate_camera_shutter(f"{output_dir}/camera_shutter.wav")
    print("  ✓ camera_shutter.wav")

    # Lock sounds
    print("\nGenerating lock sounds...")
    generator.generate_lock(
        f"{output_dir}/lock.wav",
        lock_type="lock"
    )
    print("  ✓ lock.wav")

    generator.generate_lock(
        f"{output_dir}/unlock.wav",
        lock_type="unlock"
    )
    print("  ✓ unlock.wav")

    # Tick-tock clock
    print("\nGenerating tick-tock clock sound...")
    generator.generate_tick_tock(f"{output_dir}/tick_tock.wav", cycles=3)
    print("  ✓ tick_tock.wav")

    # Bubble sounds
    print("\nGenerating bubble sounds...")
    generator.generate_bubble(
        f"{output_dir}/bubble_pop.wav",
        bubble_type="pop"
    )
    print("  ✓ bubble_pop.wav")

    generator.generate_bubble(
        f"{output_dir}/bubble_small.wav",
        bubble_type="small"
    )
    print("  ✓ bubble_small.wav")

    generator.generate_bubble(
        f"{output_dir}/bubble_large.wav",
        bubble_type="large"
    )
    print("  ✓ bubble_large.wav")

    print("\n" + "=" * 50)
    print(f"Successfully generated {len(list(output_dir.glob('*.wav')))} sound files!")
    print(f"All files are in: {output_dir}/")
    print("\nThese sounds are royalty-free and can be used in any project.")


if __name__ == "__main__":
    main()
