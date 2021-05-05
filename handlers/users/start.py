from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline import change_lan

from loader import dp, _
from utils.db_api.db_commands import update_user_language


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = _("Привет, {user}!").format(user=message.from_user.full_name)
    await message.answer(text=text, reply_markup=change_lan)

@dp.callback_query_handler(text_contains="lan")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    lan = call.data[-2:]
    text = _("Вы поменяли язык!")
    await update_user_language(id=call.from_user.id, language=lan)
    await call.message.answer(text=text)