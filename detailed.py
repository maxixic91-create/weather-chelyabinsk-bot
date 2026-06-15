"""
Handlers package for Chelyabinsk Weather Bot
All user interaction handlers
"""

from .start import router as start_router
from .menu import router as menu_router
from .forecast import router as forecast_router
from .detailed import router as detailed_router
from .radar import router as radar_router
from .navigation import router as navigation_router

__all__ = [
    'start_router',
    'menu_router',
    'forecast_router',
    'detailed_router',
    'radar_router',
    'navigation_router'
]
