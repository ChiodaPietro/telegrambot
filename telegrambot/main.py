import constants as keys
from telegram.ext import *
import responses as R

print("bot started")


def start_command(update, context):
    update.message.reply_text("reply something random to get started")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, user_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    #dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()#bots delay to check user inputs
    updater.idle()

main()