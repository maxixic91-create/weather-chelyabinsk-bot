"""
Main menu keyboard with all sections
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import FORECAST_7DAY, FORECAST_DETAILED, SHOW_RADAR, CB_EXIT

def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Create main menu keyboard with all options"""
    buttons = [
        [
            InlineKeyboardButton(
                text="🌤 Погода на 7 дней",
                callback_data=FORECAST_7DAY
            )
        ],
        [
            InlineKeyboardButton(
                text="📊 Подробная погода",
                callback_data=FORECAST_DETAILED
            )
        ],
        [
            InlineKeyboardButton(
                text="🗺 Информация",
                callback_data=SHOW_RADAR
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ Завершить",
                callback_data=CB_EXIT
            )
        ]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)
