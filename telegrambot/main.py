import constants as keys
from telegram.ext import *
import responses as R
import rock_paper_cesar as Game

print("bot started")


def start_command(update, context):
    update.message.reply_text("reply something random to get started")


def handle_message(update, context):
    text = str(update.message.text).lower() #the text is equal to THE INPUT TEXT(update.message.text)
    response = R.sample_responses(text)     #the response is eqaul to class RESPNSES.SAMPLE RESPONSES giving text input as prameter
    update.message.reply_text(response)     #reply to the user using the update (telegram function) and reply text using the response

def error(update, context):
    print(f"update {update} caused error {context.error}")


def help_command(update, context):
    update.message.reply_text("/start :to get started\n"
          "/game :to play a game")

def game_command(update,context):
    Game.game(update, context)

def main():
    updater = Updater(keys.API_KEY)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))#this is a command, it MUST START WITH A SLASH
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("game", game_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()#bots delay to check user inputs
    updater.idle()

main()