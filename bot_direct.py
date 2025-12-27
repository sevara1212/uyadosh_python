#!/usr/bin/env python3
"""Direct bot runner - use this for testing"""

from bot import bot_run

if __name__ == '__main__':
    print("=" * 50)
    print("UYADOSH BOT - Starting")
    print("=" * 50)
    print("\nBot will now listen for commands.")
    print("Try sending: /start, /help, /suggest, /about")
    print("\nPress Ctrl+C to stop the bot\n")
    print("=" * 50)
    
    bot_run()

