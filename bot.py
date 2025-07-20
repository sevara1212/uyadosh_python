from telethon import TelegramClient, events, Button
import asyncio

# Replace these with your actual credentials
api_id = 27884995   
bot_token = '7977727899:AAFuZ116BnslKa5eronyRL7qZhxvCUYaPNQ'
api_hash = '87cbf2e01613bf08ba2c59970396ffcd'

# Create the bot client
bot = TelegramClient('bot.session', api_id, api_hash)

# Handle /start command
@bot.on(events.NewMessage(pattern='/start'))
async def handler(event):
    welcome_message = (
        "Welcome to Muvr.u — your social fitness platform 🏃‍♀️⚽🧘.\n"
        "Find nearby workouts, runs, matches, and more.\n"
        "Filter by sport, age, or vibe. Choose who joins. Stay motivated.\n\n"
        "Move. Match. Motivate 🚀.\n"
        "Tap Start to explore activities around you."
    )
    miniapp_url = "https://t.me/@muvru_bot?startapp"  # Replace with your actual mini app URL
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
