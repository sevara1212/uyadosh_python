# Uyadosh Bot

A Telegram bot for the Uyadosh flatmate/room rental app.

## Setup

### Requirements
- Python 3.7+
- Dependencies: `pip install -r requirements.txt`

### Installation
```bash
pip install -r requirements.txt
```

## Running the Bot

### Option 1: Run with Flask (Recommended for Production)
```bash
python main.py
```

This runs the bot and Flask server together:
- Bot listens for Telegram commands at http://localhost:5001
- Flask server runs on port 5001

### Option 2: Run Bot Only (Development)
```bash
python -c "from bot import bot_run; bot_run()"
```

Or create a simple script:
```bash
python bot_direct.py
```

## Bot Commands

- `/start` - Welcome message with app access
- `/help` - Help menu with all commands
- `/suggest` - Send feedback and suggestions
- `/about` - Learn about Uyadosh

## Bot Details

- **Bot Name:** Uyadosh
- **Bot Username:** @uyadosh_bot
- **Bot Token:** 7052474635:AAH9-T1d5d__TCrEYJsKeDFOmBDBXGBEqzA

## Troubleshooting

If the bot isn't responding:
1. Make sure the bot is running: `python main.py` or `python bot_direct.py`
2. Check console output for errors
3. Make sure you're sending commands to @uyadosh_bot
4. Verify the bot token in bot.py matches your Telegram bot token

## Testing

To test if the bot is configured correctly:
```bash
python test_bot.py
```

This will verify the connection and show bot details.

