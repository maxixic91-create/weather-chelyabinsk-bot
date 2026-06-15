#!/usr/bin/env python3
"""
Chelyabinsk Weather Telegram Bot
Full production-ready version with web server for Render.com
"""

import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web
from config import BOT_TOKEN, WEBHOOK_PATH, WEB_SERVER_PORT

# Import all handlers
from handlers import (
    start_router,
    menu_router,
    forecast_router,
    detailed_router,
    radar_router,
    navigation_router
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Global instances
bot = None
dp = None

async def health_check(request):
    """Health check endpoint for Render"""
    return web.Response(text="OK", status=200)

async def webhook_handler(request):
    """Handle Telegram webhook (if needed)"""
    return web.Response(text="Webhook is disabled, using polling", status=200)

async def start_web_server():
    """Start aiohttp web server for health checks"""
    app = web.Application()
    app.router.add_get('/health', health_check)
    app.router.add_post(WEBHOOK_PATH, webhook_handler)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', WEB_SERVER_PORT)
    await site.start()
    logger.info(f"🌐 Web server started on port {WEB_SERVER_PORT}")
    logger.info(f"✅ Health check: http://localhost:{WEB_SERVER_PORT}/health")

async def on_startup():
    """Actions to perform on bot startup"""
    logger.info("=" * 50)
    logger.info("🤖 Chelyabinsk Weather Bot Starting...")
    logger.info("=" * 50)
    
    # Get bot info
    bot_info = await bot.get_me()
    logger.info(f"📱 Bot: @{bot_info.username}")
    logger.info(f"🆔 Bot ID: {bot_info.id}")
    
    # Start web server
    await start_web_server()
    
    logger.info("✅ Bot is ready to receive updates")
    logger.info("📊 Available commands: /start, /help")

async def on_shutdown():
    """Actions to perform on bot shutdown"""
    logger.info("🛑 Bot is shutting down...")
    
    if bot and bot.session:
        await bot.session.close()
    
    logger.info("👋 Goodbye!")

async def main():
    """Main entry point"""
    global bot, dp
    
    try:
        # Initialize bot and dispatcher
        bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
        dp = Dispatcher(storage=MemoryStorage())
        
        # Register all routers
        dp.include_router(start_router)
        dp.include_router(menu_router)
        dp.include_router(forecast_router)
        dp.include_router(detailed_router)
        dp.include_router(radar_router)
        dp.include_router(navigation_router)
        
        # Register startup/shutdown events
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        
        # Start polling
        logger.info("🚀 Starting long polling...")
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        raise
    finally:
        if bot and bot.session:
            await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
