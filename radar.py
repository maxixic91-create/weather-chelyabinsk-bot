"""
Start and help command handlers
"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.main_menu import get_main_menu_keyboard
from config import BOT_VERSION

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    """Handle /start command - welcome message"""
    welcome_text = (
        "🌤 <b>Добро пожаловать в Челябинск Погода!</b>\n\n"
        "Я предоставляю точный прогноз погоды для всех районов Челябинска.\n\n"
        "📍 <b>Доступные районы:</b>\n"
        "• Центральный (центр города)\n"
        "• Калининский (северо-запад)\n"
        "• Курчатовский (север)\n"
        "• Ленинский (юго-запад)\n"
        "• Металлургический (юг)\n"
        "• Советский (юго-запад)\n"
        "• Тракторозаводский (восток)\n\n"
        "<b>📊 Функции бота:</b>\n"
        "🌤 Прогноз на 7 дней\n"
        "📊 Почасовой детальный прогноз\n"
        "🗺 Информация о погоде\n"
        "💡 Автоматические рекомендации\n\n"
        f"<i>Версия {BOT_VERSION}</i>\n\n"
        "👇 <b>Выберите нужный раздел:</b>"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu_keyboard())

@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help command - help information"""
    help_text = (
        "❓ <b>Помощь по использованию бота</b>\n\n"
        "<b>📋 Доступные команды:</b>\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать эту справку\n"
        "/menu - Показать главное меню\n"
        "/cancel - Отменить текущее действие\n\n"
        "<b>🎯 Основные разделы:</b>\n"
        "🌤 <b>Погода на 7 дней</b>\n"
        "   Прогноз на неделю по выбранному району\n\n"
        "📊 <b>Подробная погода</b>\n"
        "   Почасовой прогноз на выбранную дату\n\n"
        "🗺 <b>Информация</b>\n"
        "   Данные о районах и источниках погоды\n\n"
        "<b>🧭 Навигация:</b>\n"
        "⬅️ Назад - вернуться в предыдущее меню\n"
        "🏠 Главное меню - вернуться в начало\n"
        "❌ Завершить - завершить сессию\n\n"
        "<b>📡 Источник данных:</b>\n"
        "Open-Meteo API (бесплатно, без ключей)\n\n"
        "<i>По вопросам и предложениям обращайтесь к разработчику</i>"
    )
    await message.answer(help_text, reply_markup=get_main_menu_keyboard())

@router.message(Command("menu"))
async def cmd_menu(message: Message):
    """Handle /menu command - show main menu"""
    await message.answer(
        "🏠 <b>Главное меню</b>\n\nВыберите нужный раздел:",
        reply_markup=get_main_menu_keyboard()
    )

@router.message(Command("cancel"))
async def cmd_cancel(message: Message):
    """Handle /cancel command - cancel current operation"""
    await message.answer(
        "✅ Действие отменено.\n\nВозвращаюсь в главное меню:",
        reply_markup=get_main_menu_keyboard()
    )
