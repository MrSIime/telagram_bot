from aiogram import Router, F
from aiogram.types import Message

from keyboards import reply, inline, builders, fabrics

router = Router()

@router.message(F.text.lower().in_(["хай", "хелоу", "привет"]))
async def greetings(message: Message):
    await message.reply("Привееееть!")


@router.message()
async def echo(message: Message):
    ...