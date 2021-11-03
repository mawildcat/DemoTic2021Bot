import sys
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

try:
    token = "1656962568:AAH1OAw1hEWDNVDA_C-gNBfO5ZL8-gN4d5s"
except Exception as e:
    print("Error 001 {}".format(e.args[0]))


try:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
except Exception as e:
    print("Error 002 {}".format(e.args[0]))

def start(bot, update):
    try:
        username = update.message.from_user.username
        message = "Hello " + username
        update.message.reply_text(message)
    except Exception as e:
        print("Error 003 {}".format(e.args[0]))


def help(bot, update):
    try:
        username = update.message.from_user.username
        update.message.reply_text('Hello {}, please send a image for classify'.format(username))
    except Exception as e:
        print("Error 004 {}".format(e.args[0]))

def getImage(bot, update):
    try:
        message = "Receiving image..."
        update.message.reply_text(message)
        print(message)

        photo_file = bot.getFile(update.message.photo[-1].file_id)
        id_user = update.message.from_user.id
        id_file = photo_file.file_id
        id_analisis = str(id_user) + "-" + str(id_file)

        filename = os.path.join('downloads/', '{}.jpg'.format(id_analisis))
        photo_file.download(filename)
        message = "Image received"
        update.message.reply_text(message)
        print(message)
        print("Waiting image..")
    except Exception as e:
        print("Error 005 {}".format(e.args[0]))


def echo(bot, update):
    try:
        update.message.reply_text(update.message.text)
        print("Receiving text...")
        print("Waiting for another test...")
        print(update.message.from_user)
    except Exception as e:
        print("Error 006 {}".format(e.args[0]))

def error(bot, update, error):
    try:
        logger.warn('Update "%s" caused error "%s"' % (update, error))
    except Exception as e:
        print("Error 007 {}".format(e.args[0]))

def main():
    try:
        print('ClassifyImagesBot init token')

        updater = Updater(token)
        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print('ClassifyImagesBot init dispatcher')

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        # on noncommand detect the document type on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, getImage))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()
        print('ClassifyImagesBot ready')
        updater.idle()
    except Exception as e:
        print("Error 008 {}".format(e.message))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error 009: {}".format(e.args[0]))
