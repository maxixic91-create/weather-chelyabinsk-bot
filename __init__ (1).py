"""
Navigation keyboards for various contexts
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CB_MAIN_MENU, CB_EXIT, CB_BACK

def get_navigation_keyboard(back_callback: str = None) -> InlineKeyboardMarkup:
    """Create navigation keyboard with optional back button"""
    buttons = []
    nav_buttons = []
    
    if back_callback:
        nav_buttons.append(
            InlineKeyboardButton(text="⬅️ Назад", callback_data=back_callback)
        )
    
    nav_buttons.append(
        InlineKeyboardButton(text="🏠 Главное меню", callback_data=CB_MAIN_MENU)
    )
    nav_buttons.append(
        InlineKeyboardButton(text="❌ Завершить", callback_data=CB_EXIT)
    )
    
    buttons.append(nav_buttons)
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_date_keyboard(dates: list) -> InlineKeyboardMarkup:
    """Create keyboard for date selection"""
    buttons = []
    
    # Add date buttons
    for date_str in dates:
        buttons.append([
            InlineKeyboardButton(text=date_str, callback_data=f"date_{date_str}")
        ])
    
    # Add navigation buttons
    buttons.append([
        InlineKeyboardButton(text="🏠 Главное меню", callback_data=CB_MAIN_MENU),
        InlineKeyboardButton(text="❌ Завершить", callback_data=CB_EXIT)
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_simple_navigation() -> InlineKeyboardMarkup:
    """Create simple navigation with only main menu and exit"""
    buttons = [[
        InlineKeyboardButton(text="🏠 Главное меню", callback_data=CB_MAIN_MENU),
        InlineKeyboardButton(text="❌ Завершить", callback_data=CB_EXIT)
    ]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
