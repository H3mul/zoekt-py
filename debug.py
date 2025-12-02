#!/usr/bin/env python
"""
Debug script for zoektpy.cli module.

Usage:
    python debug.py search <query> [options]
    python debug.py list [query] [options]
    python debug.py --help

Examples:
    python debug.py search "function" --file-header filename
    python debug.py list
    python debug.py --help
"""

import sys
from zoektpy.cli import cli


if __name__ == "__main__":
    # Pass all command-line arguments to the CLI
    cli()