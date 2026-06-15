#!/usr/bin/env python3
import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌤 <b>Челябинск Погода</b>\n\n"
        "Бот работает! Прогноз погоды для всех районов Челябинска.\n\n"
        "Функции:\n"
        "• Прогноз на 7 дней\n"
        "• Почасовой прогноз\n"
        "• Информация о погоде\n\n"
        "Выберите раздел в меню ниже:",
        parse_mode="HTML"
    )


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "❓ <b>Помощь</b>\n\n"
        "/start - начать работу\n"
        "/help - эта справка\n\n"
        "Данные от Open-Meteo API",
        parse_mode="HTML"
    )


@dp.message()
async def echo(message: Message):
    await message.answer("Используйте /start или /help")


async def main():
    logger.info("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
