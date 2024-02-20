import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from buttons import catalog
from web import audio
from turk_music import audio_turk

TOKEN = ""

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name} choose music type", reply_markup=catalog)


@dp.callback_query(F.data == "uzbek")
async def callback_query(call: CallbackQuery):
    for x in audio:
        await call.message.answer_audio(audio=x)


@dp.callback_query(F.data == "turk")
async def callback_query(call: CallbackQuery):
    for x in audio_turk:
        await call.message.answer_audio(audio=x)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
