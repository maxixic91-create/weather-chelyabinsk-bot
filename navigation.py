"""
District selection keyboards
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.districts import DISTRICTS
from config import DISTRICT_PREFIX, CB_MAIN_MENU, CB_EXIT

def get_districts_keyboard(prefix: str, show_back: bool = False) -> InlineKeyboardMarkup:
    """Create keyboard with all districts"""
    buttons = []
    
    # Add district buttons (2 per row for better layout)
    district_list = list(DISTRICTS.items())
    for i in range(0, len(district_list), 2):
        row = []
        for j in range(2):
            if i + j < len(district_list):
                key, data = district_list[i + j]
                row.append(
                    InlineKeyboardButton(
                        text=f"📍 {data['name']}",
                        callback_data=f"{prefix}{key}"
                    )
                )
        buttons.append(row)
    
    # Add navigation buttons
    nav_row = [
        InlineKeyboardButton(text="🏠 Главное меню", callback_data=CB_MAIN_MENU),
        InlineKeyboardButton(text="❌ Завершить", callback_data=CB_EXIT)
    ]
    buttons.append(nav_row)
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_districts_keyboard_with_back(
    prefix: str,
    back_callback: str
) -> InlineKeyboardMarkup:
    """Create districts keyboard with back button"""
    buttons = []
    
    # Add district buttons (2 per row)
    district_list = list(DISTRICTS.items())
    for i in range(0, len(district_list), 2):
        row = []
        for j in range(2):
            if i + j < len(district_list):
                key, data = district_list[i + j]
                row.append(
                    InlineKeyboardButton(
                        text=f"📍 {data['name']}",
                        callback_data=f"{prefix}{key}"
                    )
                )
        buttons.append(row)
    
    # Add navigation buttons with back
    nav_row = [
        InlineKeyboardButton(text="⬅️ Назад", callback_data=back_callback),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data=CB_MAIN_MENU),
        InlineKeyboardButton(text="❌ Завершить", callback_data=CB_EXIT)
    ]
    buttons.append(nav_row)
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)
