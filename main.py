import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand

API_TOKEN = '6475039438:AAGL0MkAdBwI5Gos8aAbmZD6-UetcEjwxAU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):
    bot_commands = [
        BotCommand(command="/start", description="Botti iske tusiriw")
    ]
    await bot.set_my_commands(bot_commands)
    await bot.send_message(chat_id=5563001250, text="Бот запущен")


async def on_shutdown(dp):
    await bot.send_message(chat_id=5563001250, text="Бот остановлен")
    await bot.close()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)