"""
Main menu handler
"""

from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.main_menu import get_main_menu_keyboard
from config import CB_MAIN_MENU

router = Router()

@router.callback_query(lambda c: c.data == CB_MAIN_MENU)
async def show_main_menu(callback: CallbackQuery):
    """Show main menu"""
    await callback.message.edit_text(
        "🏠 <b>Главное меню</b>\n\n"
        "Выберите нужный раздел для получения информации о погоде:",
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()
