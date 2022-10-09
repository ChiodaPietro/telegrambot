import time

from telegram.ext import *
import responses as R
import constants as keys
import random

choices = ["rock", "paper", "scissors"]


def random_choice():
    choice = random.choice(choices)
    return choice


def game(update, context):

    update.message.reply_text("the game is rock paper scissors")
    update.message.reply_text("write your choice")
    time.sleep(10)
    choice = str(update.message.text).lower()
    output = update.message.reply_text
    bot_choice = str(random_choice())
    update.message.reply_text(f"your choice is: {choice}, the bots choice is: {bot_choice}")
    if bot_choice == choice:
        output("tie")

    if bot_choice == "rock":
        if choice == "paper":
            output("YOU WON!")
        else:
            output("YOU LOST!")
    if bot_choice == "paper":
        if choice == "scissors":
            output("YOU WON!")
        else:
            output("YOU LOST")
    if bot_choice == "scissors":
        if choice == "rock":
            output("YOU LOST")
        else:
            output("YOU WON!")
