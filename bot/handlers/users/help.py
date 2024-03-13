from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp


@dp.message_handler(commands='help')
async def show_menu(message: Message):
    await message.reply(f"<b>Iltmos! Kirish uchun loginni bosing</b> \n👉🏻 /login")
