#!/usr/bin/env python3
"""Test script to verify bot connection"""

import asyncio
from telethon import TelegramClient

api_id = 27884995   
bot_token = '7052474635:AAH9-T1d5d__TCrEYJsKeDFOmBDBXGBEqzA'
api_hash = '87cbf2e01613bf08ba2c59970396ffcd'

async def test_bot():
    bot = TelegramClient('bot.session', api_id, api_hash)
    
    try:
        print("🔍 Testing bot connection...")
        print(f"API ID: {api_id}")
        print(f"Bot Token: {bot_token[:20]}...")
        
        # Try to connect
        await bot.connect()
        print("✅ Connected to Telegram")
        
        # Check if already authorized
        is_user_authorized = await bot.is_user_authorized()
        print(f"Is Authorized: {is_user_authorized}")
        
        if not is_user_authorized:
            print("\n⚠️ Starting bot with token...")
            await bot.start(bot_token=bot_token)
        
        me = await bot.get_me()
        print(f"✅ Bot is logged in as: {me.first_name}")
        print(f"   Bot ID: {me.id}")
        print(f"   Username: @{me.username}" if me.username else "")
        
        print("\n✅ Bot is working! You can now test commands:")
        print("   Send /start to see the welcome message")
        print("   Send /help for help menu")
        print("   Send /suggest to send suggestions")
        print("   Send /about for info\n")
        
        await bot.disconnect()
        print("✅ Disconnected successfully")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    asyncio.run(test_bot())

