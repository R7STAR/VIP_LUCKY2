python
import logging
import LOGGER
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re
from os import getenv
from dotenv import load_dotenv


# Define your bot token
TOKEN = getenv("BOT_TOKEN", "")

# Create an updater object
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def welcome_new_members(update, context):
    chat_id = update.message.chat_id
    new_members = update.message.new_chat_members
    for member in new_members:
        context.bot.send_message(chat_id=chat_id,
                                 text=f"Welcome {member.first_name}!"
                                 )

# Create a handler for new members joining
new_member_handler = MessageHandler(Filters.status_update.new_chat_members, welcome_new_members)
dispatcher.add_handler(new_member_handler)


# Start the bot
updater.start_polling()