from aiogram import Router

from bot.handlers.client.start import start_rt
from bot.handlers.client.currency_form import currency_form_rt
from bot.handlers.admin.startup import startup_rt


def register_routers() -> Router:
    root_rt = Router()
    root_rt.include_router(start_rt)
    root_rt.include_router(currency_form_rt)
    root_rt.include_router(startup_rt)

    return root_rt
