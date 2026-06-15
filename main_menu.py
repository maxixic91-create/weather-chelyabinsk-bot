"""
Keyboards package for all inline keyboards
"""

from .main_menu import get_main_menu_keyboard
from .districts import get_districts_keyboard, get_districts_keyboard_with_back
from .navigation import get_navigation_keyboard, get_date_keyboard

__all__ = [
    'get_main_menu_keyboard',
    'get_districts_keyboard',
    'get_districts_keyboard_with_back',
    'get_navigation_keyboard',
    'get_date_keyboard'
]
