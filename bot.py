#!/usr/bin/env python3
import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_main_menu():
    """Create main menu keyboard"""
    buttons = [
        [InlineKeyboardButton(text="🌤 Погода на 7 дней", callback_data="forecast_7day")],
        [InlineKeyboardButton(text="📊 Подробная погода", callback_data="forecast_detailed")],
        [InlineKeyboardButton(text="🗺 Информация", callback_data="info")],
        [InlineKeyboardButton(text="❌ Завершить", callback_data="exit")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_districts_menu():
    """Create districts keyboard"""
    districts = [
        "Центральный", "Калининский", "Курчатовский",
        "Ленинский", "Металлургический", "Советский", "Тракторозаводский"
    ]
    buttons = [[InlineKeyboardButton(text=d, callback_data=f"district_{d}")] for d in districts]
    buttons.append([InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌤 <b>Челябинск Погода</b>\n\n"
        "Бот работает! Прогноз погоды для всех районов Челябинска.\n\n"
        "📋 <b>Функции:</b>\n"
        "• 🌤 Прогноз на 7 дней\n"
        "• 📊 Почасовой прогноз\n"
        "• 🗺 Информация о погоде\n\n"
        "👇 <b>Выберите раздел:</b>",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "❓ <b>Помощь</b>\n\n"
        "/start - начать работу\n"
        "/help - эта справка\n\n"
        "<b>Навигация:</b>\n"
        "⬅️ Назад - вернуться\n"
        "🏠 Главное меню - в начало\n"
        "❌ Завершить - выход\n\n"
        "📡 Данные: Open-Meteo API",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )


@dp.callback_query(lambda c: c.data == "forecast_7day")
async def forecast_7day(callback):
    await callback.message.edit_text(
        "🌤 <b>Прогноз на 7 дней</b>\n\n"
        "📍 <b>Выберите район:</b>",
        parse_mode="HTML",
        reply_markup=get_districts_menu()
    )
    await callback.answer()


@dp.callback_query(lambda c: c.data == "forecast_detailed")
async def forecast_detailed(callback):
    await callback.message.edit_text(
        "📊 <b>Подробный прогноз</b>\n\n"
        "📍 <b>Выберите район:</b>",
        parse_mode="HTML",
        reply_markup=get_districts_menu()
    )
    await callback.answer()


@dp.callback_query(lambda c: c.data == "info")
async def info(callback):
    await callback.message.edit_text(
        "🗺 <b>Информация</b>\n\n"
        "📍 <b>Районы Челябинска:</b>\n"
        "• Центральный\n• Калининский\n• Курчатовский\n"
        "• Ленинский\n• Металлургический\n• Советский\n• Тракторозаводский\n\n"
        "🌤 <b>Источник:</b> Open-Meteo API\n"
        "🆓 Бесплатно, без API-ключей\n\n"
        "💡 <b>Совет:</b> Для точного прогноза выбирайте дату и район",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )
    await callback.answer()


@dp.callback_query(lambda c: c.data == "main_menu")
async def main_menu(callback):
    await callback.message.edit_text(
        "🏠 <b>Главное меню</b>\n\nВыберите раздел:",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )
    await callback.answer()


@dp.callback_query(lambda c: c.data == "exit")
async def exit_bot(callback):
    await callback.message.delete()
    await callback.answer("👋 До свидания! Нажмите /start чтобы продолжить")


@dp.callback_query(lambda c: c.data.startswith("district_"))
async def district_selected(callback):
    district = callback.data.replace("district_", "")
    await callback.message.edit_text(
        f"📍 <b>Район: {district}</b>\n\n"
        f"⏳ Прогноз загружается...\n\n"
        f"<i>Полный прогноз будет доступен в следующей версии</i>",
        parse_mode="HTML",
        reply_markup=get_districts_menu()
    )
    await callback.answer()


async def main():
    logger.info("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
