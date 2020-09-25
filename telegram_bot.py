from aiogram import Bot, Dispatcher, executor, types
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token='1189322913:AAGBfHBa_kJCvZngbUwSvRTTgsi39Nnm5pY')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message)
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)