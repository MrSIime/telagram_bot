import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message

bot = Bot("YOUR TOKEN HERE...", parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Hello, <b>{message.from_user.first_name}</b>")


@dp.message(Command(commands=["....", "..."]))
async def some_command(message: Message, command: CommandObject):
    ...


@dp.message(F.text == "...")
async def some_text(message: Message):
    ...


@dp.message()
async def echo(message: Message):
    ...


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
