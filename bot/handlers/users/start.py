from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import dp
from save import save_user, activate_user
import json


@dp.message_handler(Command('start'))
async def show_menu1(message: Message):
    usr = save_user(message)
    if usr.status_code == 201:
        usr_txt = usr.text
        await message.reply(f"<b>Status:</b> hisobingiz mafaqqiyatli yaratildi.")
    else:
        usr_txt = json.loads(usr.text)
        await message.reply(f"<b>Xolat:</b> ushbu hisob allaqachon yaratilgan.")


@dp.message_handler(Command('kirish'))
async def show_menu2(message: Message):
    usr = activate_user(message.from_user.id)
    if usr.status_code == 200:
        usr_txt = json.loads(usr.text)
        await message.reply(f"<b>Kod:</b> {usr_txt}")
    else:
        usr_txt = json.loads(usr.text)
        await message.reply(f"<b>Xolat:</b> siz to'lov qilmagansiz!")
