import subprocess
import sys


PYTHON = sys.executable

CHECKS = [
    [
        PYTHON,
        "-B",
        "-m",
        "pytest",
        "-p",
        "no:cacheprovider",
    ],
    [
        PYTHON,
        "-m",
        "ruff",
        "check",
        "main.py",
        "test_main.py",
    ],
    [
        PYTHON,
        "-m",
        "ruff",
        "format",
        "--check",
        "main.py",
        "test_main.py",
    ],
]


def main():
    for command in CHECKS:
        print(f"\nRunning: {' '.join(command)}", flush=True)

        result = subprocess.run(command, check=False)

        if result.returncode != 0:
            print("QUALITY GATE FAILED")
            return result.returncode

    print("\nQUALITY GATE PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())