from telethon import TelegramClient, events, Button
import asyncio

# Replace these with your actual credentials
api_id = 27884995   
bot_token = '7052474635:AAH9-T1d5d__TCrEYJsKeDFOmBDBXGBEqzA'
api_hash = '87cbf2e01613bf08ba2c59970396ffcd'

# Create the bot client
bot = TelegramClient('bot.session', api_id, api_hash)

# Handle /start command
@bot.on(events.NewMessage(pattern='/start'))
async def handler(event):
    welcome_message = (
        "Welcome to Uyadosh — find your perfect flatmate or room! 🏠\n"
        "Looking for someone to share your space with? Uyadosh connects you with compatible flatmates and great rooms to rent.\n"
        "Browse listings, connect with potential flatmates, and find your ideal living situation.\n\n"
        "Find. Connect. Move In 🔑\n"
        "Tap Start to explore rooms and flatmates near you."
    )
    miniapp_url = "https://t.me/@uyadosh_bot?startapp"  # Replace with your actual mini app URL
    await event.respond(
        welcome_message,
        buttons=[
            [Button.url('Start', miniapp_url)]
        ]
    )

def bot_run():
    print("Bot is running...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot.start(bot_token=bot_token)
    bot.run_until_disconnected()
