#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DicVenBot - Diccionario Venezolano
#
##########################################################################
"""DicVenBot - Diccionario Venezolano
La intención de este bot de Telegram es proveer términos en el vocabulario del venezolano.
Es una fase inicial y he extraído la data desde diferentes fuentes de internet.
Es probable que muchos términos no se encuentren por lo que se puede ir agregando.

Cuando no consigue un término, responde de manera muy venezolana :-)

Para buscar: /quevainaes {término a buscar}
ejemplo: /quevainaes **vaina**

NOTA: El autor no se hace responsable por los términos, ya que han sido recopilados de diferentes fuentes de internet.

Asdrúbal R. Velásquez Lagrave
Twitter: @Visionario
"""
from telegram import ParseMode

from telegram.ext   import    (Updater, CommandHandler, MessageHandler,
                                Filters, RegexHandler, ConversationHandler)

from functools import wraps

import logging, logging.handlers

import os, time, sys, random, json

#Import constants
from constants  import LOGFILE, TOKEN, ADMINS
from constants  import DATAFILE, RESPUESTAS_NEGATIVAS_NEUTRAL
from constants  import MSG_START, MSG_AYUDA

# ABOUT DATA
__author__ = 'Asdrubal R. Velasquez Lagrave <visionario@gmail.com>'
__twitter__ = '@Visionario'
__copyright__ = 'CopyLeft'
__credits__ = ['']
__license__ = 'GPLv3.0'
__version__ = '0.1'
__maintainer__ = 'Asdrubal R. Velasquez Lagrave'
__email__ = 'visionario@gmail.com'
__status__ = 'BETA - UNSTABLE'

# Enable logging / Create the Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create the Handler for logging data to a file
logger_handler = logging.handlers.WatchedFileHandler(LOGFILE)
logger_handler.setLevel(logging.INFO)

# Create a Formatter for formatting the log messages
logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the Formatter to the Handler
logger_handler.setFormatter(logger_formatter)

# Add the Handler to the Logger
logger.addHandler(logger_handler)

# SCREEN LOG
logger_handler_screen = logging.StreamHandler()
logger_handler_screen.setLevel(logging.DEBUG)
logger.addHandler(logger_handler_screen)




# DATAFILE es el archivo de datos que se encuentra en json
with open(DATAFILE) as data_file:
    DATA = json.load(data_file)



# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#restrict-access-to-a-handler-decorator
def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(bot, update, *args, **kwargs)
    return wrapped




# Comando Start.
def start(bot, update):
    chat_id = update.message.chat_id
    user = update.message.from_user
    update.message.reply_text(MSG_START % user.first_name, parse_mode=ParseMode.MARKDOWN)
    logger.info("START: chat_id:%s user_id:%s Usuario:%s Username:@%s data:%s" % (chat_id, user.id, user.first_name, user.username, update.message.text))


# Ayuda
def ayuda(bot, update):
    chat_id = update.message.chat_id        #Chat ID
    user_id = update.message.from_user.id   #User ID
    user = update.message.from_user         #user

    # Haga un Log de esto
    logger.info("Texto: chat_id:%s user_id:%s Usuario:%s Username:@%s data:%s" % (chat_id, user_id, user.first_name, user.username, update.message.text))

    update.message.reply_text(MSG_AYUDA, parse_mode=ParseMode.MARKDOWN)



#   Se recibe el parámetro a buscar
def quevainaes(bot, update):
    chat_id = update.message.chat_id        #Chat ID
    user_id = update.message.from_user.id   #User ID
    user = update.message.from_user         #user
    # WHOAMI? (bot)
    ME = bot.getMe()

    text = update.message.text

    # Verifique si el comando viene con sufijo (/command@bot.username) y prepare
    if (ME['username'] in text):
        text = text.split(ME['username'])[1][1:]
    else:
        text = text[len(text.split()[0])+1:]

    if not text:    # Se recibió un comando sin texto
        return      # ignore

    # Haga un Log de esto
    logger.info("Texto: chat_id:%s user_id:%s Usuario:%s Username:@%s data:%s" % (chat_id, user_id, user.first_name, user.username, update.message.text))

    try: # Intenta buscar
        data = DATA[text.lower()]
        #   Envíe el resultado (si lo encontró)
        header = "👇***" + text.capitalize() + "***👇\n"
        update.message.reply_text(header + data, parse_mode=ParseMode.MARKDOWN)
    except:
        #   Respuesta aleatoria, elegida desde el archivo de constantes
        #   Se intenta hacerlo un poco jocoso dada la temática de este bot
        #   Existen tres conatantes que se pueden usar
        #   RESPUESTAS_NEGATIVAS_NEUTRAL
        #   TODO: RESPUESTAS_NEGATIVAS_MASCULINO
        #   TODO: RESPUESTAS_NEGATIVAS_FEMENINO
        #   Solo en una futura versión se le puede preguntar al usuario si es
        #   hombre o mujer para afinar las respuestas del bot adecuadamente
        r = RESPUESTAS_NEGATIVAS_NEUTRAL[random.randrange(0,len(RESPUESTAS_NEGATIVAS_NEUTRAL))]
        update.message.reply_text(r, parse_mode=ParseMode.MARKDOWN)
        logger.info("NO EXISTE: chat_id:%s user_id:%s Usuario:%s Username:@%s data:%s" % (chat_id, user_id, user.first_name, user.username, update.message.text))



# Restart
# Restringido solo para ADMIN (Constante ADMINS)
@restricted
def restart(bot, update ):
    chat_id = update.message.chat_id        #Chat ID
    user_id = update.message.from_user.id   #User ID
    user = update.message.from_user         #user

    bot.send_message(update.message.chat_id, "Bot is restarting...")
    logger.info("RESTART FROM: chat_id:%s user_id:%s Usuario:%s Username:@%s data:%s" % (chat_id, user_id, user.first_name, user.username, update.message.text))
    time.sleep(0.5)
    os.execl(sys.executable, sys.executable, *sys.argv)



def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))



# Main function
def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("restart", restart))
    dp.add_handler(CommandHandler("ayuda", ayuda))
    dp.add_handler(CommandHandler(["q","quevainaes","quevergaes","buscar","define"], quevainaes))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()


    # NOTIFY ADMINS BOT IS ONLINE
    for admin in ADMINS:
        updater.bot.send_message(admin, "@" + updater.bot.getMe().username + " En línea!!")

    logger.info("BOT " + "@" + updater.bot.getMe().username + " INICIADO ")


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

