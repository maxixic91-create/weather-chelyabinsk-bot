#!/usr/bin/env python3
import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiohttp import web
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ============ КЛАВИАТУРЫ ============

def get_main_menu():
    buttons = [
        [InlineKeyboardButton(text="🌤 Погода на 7 дней", callback_data="forecast_7day")],
        [InlineKeyboardButton(text="📊 Подробная погода", callback_data="forecast_detailed")],
        [InlineKeyboardButton(text="🗺 Информация", callback_data="info")],
        [InlineKeyboardButton(text="❌ Завершить", callback_data="exit")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_districts_menu(back_callback="main_menu"):
    districts = ["Центральный", "Калининский", "Курчатовский", "Ленинский", "Металлургический", "Советский", "Тракторозаводский"]
    buttons = [[InlineKeyboardButton(text=f"📍 {d}", callback_data=f"district_{d}")] for d in districts]
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data=back_callback)])
    buttons.append([InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_dates_menu():
    from datetime import datetime, timedelta
    dates = []
    today = datetime.now()
    for i in range(7):
        d = today + timedelta(days=i)
        if i == 0:
            dates.append(f"Сегодня ({d.strftime('%d.%m')})")
        elif i == 1:
            dates.append(f"Завтра ({d.strftime('%d.%m')})")
        else:
            dates.append(d.strftime("%d.%m"))
    buttons = [[InlineKeyboardButton(text=d, callback_data=f"date_{d}")] for d in dates]
    buttons.append([InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ============ КОМАНДЫ ============

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌤 <b>Челябинск Погода</b>\n\n"
        "📍 <b>Районы:</b> Центральный, Калининский, Курчатовский,\n"
        "Ленинский, Металлургический, Советский, Тракторозаводский\n\n"
        "👇 <b>Выберите раздел:</b>",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )

@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "❓ <b>Помощь</b>\n\n"
        "/start - начать работу\n"
        "/help - эта справка\n\n"
        "<b>Навигация:</b>\n"
        "⬅️ Назад - вернуться\n"
        "🏠 Главное меню - в начало\n"
        "❌ Завершить - выход\n\n"
        "📡 Данные: Open-Meteo API (бесплатно)",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )

# ============ CALLBACK HANDLERS ============

@dp.callback_query(lambda c: c.data == "forecast_7day")
async def forecast_7day(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌤 <b>Прогноз на 7 дней</b>\n\n"
        "📍 <b>Выберите район:</b>",
        parse_mode="HTML",
        reply_markup=get_districts_menu("main_menu")
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "forecast_detailed")
async def forecast_detailed(callback: CallbackQuery):
    await callback.message.edit_text(
        "📊 <b>Подробный почасовой прогноз</b>\n\n"
        "📅 <b>Шаг 1:</b> Выберите дату:",
        parse_mode="HTML",
        reply_markup=get_dates_menu()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data.startswith("date_"))
async def date_selected(callback: CallbackQuery):
    date = callback.data.replace("date_", "")
    await callback.message.edit_text(
        f"📅 <b>Выбрана дата:</b> {date}\n\n"
        f"📍 <b>Шаг 2:</b> Выберите район:",
        parse_mode="HTML",
        reply_markup=get_districts_menu("forecast_detailed")
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "info")
async def info(callback: CallbackQuery):
    await callback.message.edit_text(
        "🗺 <b>Информация</b>\n\n"
        "📍 <b>Районы Челябинска:</b>\n"
        "• Центральный (центр города)\n"
        "• Калининский (северо-запад)\n"
        "• Курчатовский (север)\n"
        "• Ленинский (юго-запад)\n"
        "• Металлургический (юг)\n"
        "• Советский (юго-запад)\n"
        "• Тракторозаводский (восток)\n\n"
        "🌤 <b>Источник:</b> Open-Meteo API\n"
        "🆓 Бесплатно, без API-ключей\n"
        "🔄 Обновление: каждые 30 минут\n\n"
        "💡 <b>Совет:</b> Для точного прогноза\n"
        "выбирайте дату, затем район",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "main_menu")
async def main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "🏠 <b>Главное меню</b>\n\nВыберите нужный раздел:",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "exit")
async def exit_bot(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer("👋 До свидания! Нажмите /start чтобы продолжить")

@dp.callback_query(lambda c: c.data.startswith("district_"))
async def district_selected(callback: CallbackQuery):
    district = callback.data.replace("district_", "")
    await callback.message.edit_text(
        f"📍 <b>Район: {district}</b>\n\n"
        f"⏳ <i>Прогноз загружается...</i>\n\n"
        f"🌡 Температура: загрузка...\n"
        f"🌧 Осадки: загрузка...\n"
        f"💨 Ветер: загрузка...\n\n"
        f"<i>Полный прогноз будет доступен в следующем обновлении</i>",
        parse_mode="HTML",
        reply_markup=get_districts_menu("main_menu")
    )
    await callback.answer()

# ============ ВЕБ-СЕРВЕР ДЛЯ RENDER ============

async def health_check(request):
    return web.Response(text="OK", status=200)

async def start_web_server():
    app = web.Application()
    app.router.add_get('/health', health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    logger.info("🌐 Web server started on port 8080")

# ============ MAIN ============

async def main():
    await start_web_server()
    logger.info("🤖 Starting bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
