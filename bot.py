import sys
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = "2027163737:AAEVzQD89QfRai3LNJ6kCRUPFH-EClI2278"

def start(bot, update):
    try:
        username = update.message.from_user.username
        message = "Hola " + username + ", bienvenido a este robot creado por MaWildcat"
        update.message.reply_text(message)
    except Exception as e:
        print("Error 001 {}".format(e.args[0]))


def echo(bot, update):
    try:
        text = update.message.text
        update.message.reply_text(text)
    except Exception as e:
        print("Error 002 {}".format(e.args[0]))

def help(bot, update):
    try:
        message = "Puedes enviar textos o imágenes"
        update.message.reply_text(message)
    except Exception as e:
        print("Error 003 {}".format(e.args[0]))


def error(bot, update, error):
    try:
        print(error)
    except Exception as e:
        print("Error 004 {}".format(e.args[0]))

def getImage(bot, update):
    try:
        message = "Recibiendo imágen"
        update.message.reply_text(message)

        file = bot.getFile(update.message.photo[-1].file_id)
        id = file.file_id

        filename = os.path.join("descargas/", "{}.jpg".format(id))
        file.download(filename)

        message = "Imagen guardada"
        update.message.reply_text(message)


    except Exception as e:
        print("Error 007 {}".format(e.args[0]))


def main():
    try:
        updater = Updater(token)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, getImage))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()
        print("Bot listo")
    except Exception as e:
        print("Error 005 {}".format(e.message))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error 006 {}".format(e.args[0]))
