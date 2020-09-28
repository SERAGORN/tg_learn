from aiogram import Bot, Dispatcher, executor, types
import logging
import asyncio

loop = asyncio.get_even_loop()
logging.basicConfig(level=logging.INFO)

bot = Bot(token='1189322913:AAGBfHBa_kJCvZngbUwSvRTTgsi39Nnm5pY')
dp = Dispatcher(bot, loop=loop)

@dp.message_handler()
async def echo(message: types.Message)
    await message.answer(text='Hi')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
