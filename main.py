"""
WhatsApp Message Repeater / Desktop Auto-Sender
------------------------------------------------
Automates typing and sending repetitive messages into desktop WhatsApp
(or WhatsApp Web) using pyautogui and time.

Safety Features:
- PyAutoGUI Failsafe: Moving your mouse cursor to any corner of the screen immediately aborts the script.
- Ctrl+C handling: Gracefully stops the script when interrupted from the terminal.
"""

import sys
import time
import pyautogui

# ==============================================================================
# CONFIGURATION SETTINGS
# Modify these default values or use the interactive prompt when running.
# ==============================================================================
DEFAULT_MESSAGE = "Mama Oyata adarei ne menike ❤️"  # The message text to send
DEFAULT_REPEAT_COUNT = 500                               # Total number of times to repeat
DEFAULT_DELAY = 0.5                                     # Delay in seconds between messages
DEFAULT_COUNTDOWN = 5                                   # Countdown time in seconds to switch to WhatsApp
TYPING_INTERVAL = 0.01                                  # Delay between keystrokes (prevents missed letters)

# Enable PyAutoGUI fail-safe (move mouse to any corner of the screen to trigger an emergency stop)
pyautogui.FAILSAFE = True


def get_configuration():
    """
    Allows the user to either use predefined configurations or specify new ones
    interactively through the terminal.
    """
    print("=" * 60)
    print("      WHATSAPP MESSAGE REPEATER / AUTO-TYPER TOOL")
    print("=" * 60)
    print("Current Configuration:")
    print(f" - Message       : \"{DEFAULT_MESSAGE}\"")
    print(f" - Repeat Count  : {DEFAULT_REPEAT_COUNT}")
    print(f" - Delay (sec)   : {DEFAULT_DELAY}s")
    print(f" - Countdown     : {DEFAULT_COUNTDOWN}s")
    print("=" * 60)

    try:
        choice = input("Use default settings? [Y/n] (Press Enter for Yes): ").strip().lower()
        if choice not in ("n", "no"):
            return DEFAULT_MESSAGE, DEFAULT_REPEAT_COUNT, DEFAULT_DELAY, DEFAULT_COUNTDOWN

        # Interactive configuration inputs
        print("\nEnter custom settings:")
        message = input(f"Enter message text [{DEFAULT_MESSAGE}]: ").strip()
        if not message:
            message = DEFAULT_MESSAGE

        count_input = input(f"Enter repeat count [{DEFAULT_REPEAT_COUNT}]: ").strip()
        count = int(count_input) if count_input else DEFAULT_REPEAT_COUNT

        delay_input = input(f"Enter delay between messages in seconds [{DEFAULT_DELAY}]: ").strip()
        delay = float(delay_input) if delay_input else DEFAULT_DELAY

        countdown_input = input(f"Enter countdown seconds [{DEFAULT_COUNTDOWN}]: ").strip()
        countdown = int(countdown_input) if countdown_input else DEFAULT_COUNTDOWN

        return message, count, delay, countdown

    except ValueError as e:
        print(f"[!] Invalid input entered ({e}). Reverting to default configuration.")
        return DEFAULT_MESSAGE, DEFAULT_REPEAT_COUNT, DEFAULT_DELAY, DEFAULT_COUNTDOWN


def countdown_timer(seconds: int):
    """
    Displays a countdown in the console to allow switching to WhatsApp
    and focusing on the message input box.
    """
    print(f"\n[!] You have {seconds} seconds to switch to WhatsApp.")
    print("[!] CLICK ON THE WHATSAPP MESSAGE INPUT BOX NOW!\n")
    print("=" * 60)
    print("NOTE: Emergency Stop available at any time:")
    print("  -> Move mouse to ANY corner of your screen OR press Ctrl+C")
    print("=" * 60 + "\n")

    for remaining in range(seconds, 0, -1):
        print(f"[*] Starting in {remaining} second(s)...", end="\r", flush=True)
        time.sleep(1)

    print("\n[*] Timer finished! Commencing message loop now...\n")


def send_messages(message: str, repeat_count: int, delay: float):
    """
    Executes the loop to type and send messages using pyautogui.
    """
    print(f"[*] Target: Sending {repeat_count} message(s) with {delay}s delay between each.")
    print("-" * 60)

    start_time = time.time()
    sent_count = 0

    try:
        for i in range(1, repeat_count + 1):
            # Step 1: Type the message
            pyautogui.write(message, interval=TYPING_INTERVAL)

            # Step 2: Press 'enter' to send
            pyautogui.press("enter")

            sent_count = i
            # Step 3: Console print statement to track progress
            print(f"[+] Sent message {i} of {repeat_count}")

            # Step 4: Delay before next message (skip delay after final message)
            if i < repeat_count:
                time.sleep(delay)

        elapsed = time.time() - start_time
        print("-" * 60)
        print(f"[SUCCESS] All {sent_count} messages sent successfully in {elapsed:.2f} seconds!")

    except pyautogui.FailSafeException:
        print("\n[ABORTED] Emergency stop triggered! Mouse cursor moved to screen corner.")
    except KeyboardInterrupt:
        print(f"\n[ABORTED] Process interrupted by user (Ctrl+C). Successfully sent {sent_count} of {repeat_count} messages.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")


def main():
    try:
        message, repeat_count, delay, countdown = get_configuration()
        countdown_timer(countdown)
        send_messages(message, repeat_count, delay)
    except KeyboardInterrupt:
        print("\n[ABORTED] Program exited before start.")
        sys.exit(0)


if __name__ == "__main__":
    main()
