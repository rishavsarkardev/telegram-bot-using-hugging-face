import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, FSInputFile

from huggingface_apis.text_generation import generate_text_response
from huggingface_apis.image_generation import generate_fast_image

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "8652907478:AAGkkb_4qPS4I1b-Ah4-LKhKCBKYNgdcYAw"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command("image"))
async def image_handler(message: Message, command: CommandObject) -> None:
    """
    Generates an image based on user's prompt
    """
    try:
        prompt = command.args
        photo_generated = generate_fast_image(prompt, message.chat.id)
        if photo_generated:
            photo = FSInputFile(f"./images/{str(message.chat.id)}.png")
            await message.answer_photo(photo)
            os.remove(f"./images/{message.chat.id}.png")
        else:
            await message.answer("An unexpected error occurred")

    except Exception as e:
        print(e)
        return "An unexpected error occurred"


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Replies to the user's normal messages using the "Qwen2.5-0.5B-Instruct" Model
    """
    try:
        fetched_answer = generate_text_response(message.text)
        await message.answer(fetched_answer)
    except Exception as e:
        print(e)
        # But not all the types is supported to be copied so need to handle it
        await message.answer("An unexpected error occurred")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())