from telethon import TelegramClient, events, Button
import asyncio

# Replace these with your actual credentials
api_id = 27884995   
bot_token = '7052474635:AAH9-T1d5d__TCrEYJsKeDFOmBDBXGBEqzA'
api_hash = '87cbf2e01613bf08ba2c59970396ffcd'

# Create the bot client
bot = TelegramClient('bot.session', api_id, api_hash)

# Handle /start command
@bot.on(events.NewMessage(pattern=r'^/start'))
async def start_handler(event):
    print(f"[/start] Received from {event.sender_id}")
    welcome_message = (
        "Welcome to Uyadosh — find your perfect flatmate or room! 🏠\n\n"
        "Looking for someone to share your space with? Uyadosh connects you with compatible flatmates and great rooms to rent.\n"
        "Browse listings, connect with potential flatmates, and find your ideal living situation.\n\n"
        "✨ Find. Connect. Move In 🔑\n\n"
        "Tap the button below to explore rooms and flatmates near you, or use /help to learn more!"
    )
    miniapp_url = "https://t.me/@uyadosh_bot?startapp"
    try:
        await event.respond(
            welcome_message,
            buttons=[
                [Button.url('🚀 Open Uyadosh', miniapp_url)],
                [Button.text('/help')]
            ]
        )
        print(f"[/start] Response sent successfully")
    except Exception as e:
        print(f"[/start] Error: {e}")

# Handle /help command
@bot.on(events.NewMessage(pattern=r'^/help'))
async def help_handler(event):
    print(f"[/help] Received from {event.sender_id}")
    help_message = (
        "📋 Uyadosh Help Menu\n\n"
        "Here are the commands you can use:\n\n"
        "🏠 /start - Welcome message and app access\n"
        "❓ /help - This help menu\n"
        "💬 /suggest - Send us your feedback or suggestions\n"
        "ℹ️ /about - Learn more about Uyadosh\n\n"
        "How to use Uyadosh:\n"
        "1. Tap 'Open Uyadosh' to access the web app\n"
        "2. Create your profile (flatmate or room listing)\n"
        "3. Browse compatible matches\n"
        "4. Connect with potential flatmates\n"
        "5. Schedule viewings or meetings\n\n"
        "Have a question? Use /suggest to send us feedback!"
    )
    try:
        await event.respond(help_message)
        print(f"[/help] Response sent successfully")
    except Exception as e:
        print(f"[/help] Error: {e}")

# Handle /suggest command
@bot.on(events.NewMessage(pattern=r'^/suggest'))
async def suggest_handler(event):
    print(f"[/suggest] Received from {event.sender_id}")
    suggest_message = (
        "💡 We'd love to hear from you!\n\n"
        "Please reply to this message with your suggestions, feedback, or feature requests. "
        "Your input helps us make Uyadosh better!\n\n"
        "What would you like to suggest?"
    )
    try:
        await event.respond(suggest_message)
        print(f"[/suggest] Response sent successfully")
    except Exception as e:
        print(f"[/suggest] Error: {e}")

# Handle /about command
@bot.on(events.NewMessage(pattern=r'^/about'))
async def about_handler(event):
    print(f"[/about] Received from {event.sender_id}")
    about_message = (
        "ℹ️ About Uyadosh\n\n"
        "Uyadosh is a modern platform designed to solve the challenge of finding the perfect flatmate or room.\n\n"
        "Why Uyadosh?\n"
        "✓ Find compatible flatmates based on interests & lifestyle\n"
        "✓ Browse verified room listings\n"
        "✓ Safe and secure connections\n"
        "✓ Easy messaging and scheduling\n\n"
        "Whether you're looking for a flatmate or renting a room, Uyadosh makes the process simple and stress-free.\n\n"
        "Get started: /start"
    )
    try:
        await event.respond(about_message)
        print(f"[/about] Response sent successfully")
    except Exception as e:
        print(f"[/about] Error: {e}")

async def start_bot():
    """Start the bot asynchronously"""
    try:
        print("🤖 Uyadosh Bot is starting...")
        print(f"Bot Token: {bot_token[:20]}...")
        print(f"API ID: {api_id}")
        
        # Connect and start
        await bot.start(bot_token=bot_token)
        print("✅ Bot successfully connected!")
        print("Listening for /start, /help, /suggest, and /about commands...")
        print("Waiting for messages...\n")
        
        # Run until disconnected
        await bot.run_until_disconnected()
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        import traceback
        traceback.print_exc()

def bot_run():
    """Run the bot"""
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
