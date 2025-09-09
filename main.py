#!/usr/bin/env python3
"""
Professional Unit Converter
----------------------------
A robust and extensible unit conversion tool designed with clarity and efficiency in mind.
Because precision matters, and good code should speak for itself.

"""

import sys
from src.interface.cli import Interface


def main():
    """
    Entry point. Simple, clean, effective.
    Good architecture means the main function is almost trivial.
    """
    try:
        app = Interface()
        app.run()
    except Exception as e:
        print(f"\n⚠ Unexpected error: {e}")
        print("  The application will now exit.")
        sys.exit(1)


if __name__ == "__main__":
    main()