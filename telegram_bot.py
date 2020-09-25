from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

updater = Updater(token='1189322913:AAGBfHBa_kJCvZngbUwSvRTTgsi39Nnm5pY', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Where is Febonacci???")      

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Where is Febonacci???")

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling(poll_interval=0.0, timeout=10, clean=False, bootstrap_retries=-1, read_latency=2.0, allowed_updates=None)