"""caffeine-py entry point."""

import argparse
import ctypes
import os
import platform
import random
import shutil
import string
import sys
import time


def keep_awake():
    system = platform.system()

    if system == "Windows":
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001
        ES_DISPLAY_REQUIRED = 0x00000002
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
        )

    elif system == "Darwin":  # macOS
        os.system("caffeinate -u -t 30")

    elif system == "Linux":
        if shutil.which("systemd-inhibit"):
            os.system("systemd-inhibit --what=idle --mode=block sleep 1 &")
        elif shutil.which("xdotool"):
            os.system("xdotool key Shift")
        else:
            print("⚠️  No known keep-awake method found for Linux.")


def matrix_line(width=80):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(width))


def run(interval: int):
    print("\033[92m☕ caffeine-py is active. Your system will stay awake.\033[0m")
    print("\033[90mPress Ctrl+C to exit.\033[0m\n")

    try:
        while True:
            keep_awake()
            print("\033[92m" + matrix_line(80) + "\033[0m")  # green "Matrix" line
            sys.stdout.flush()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n👋 Caffeine stopped.")


def main():
    parser = argparse.ArgumentParser(description="Keep your system awake (cross-platform).")
    parser.add_argument(
        "-i", "--interval",
        type=int,
        default=5,
        help="Interval in seconds between keep-awake signals (default: 5)"
    )
    args = parser.parse_args()
    run(args.interval)


if __name__ == "__main__":
    main()
