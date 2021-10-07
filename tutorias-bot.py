import logging
import os
from telegram import Update, ForceReply, message, InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    ID = update.message.from_user.id

    update.message.chat.send_action(
        action=ChatAction.TYPING,
        timeout=None
    )

    context.bot.send_message(
        chat_id = ID,
        text = 'Hola, te puedo ayudar en lo siguiente',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Trámites', callback_data='tramites')],
            [InlineKeyboardButton(text='📚 Bibliografía', callback_data='bibliografia')],
            [InlineKeyboardButton(text='🏫🚌 ¿Cómo llego?', callback_data='ubicacion')]
            
        ])
    )

def reinicio(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Te puedo ayudar en lo siguiente:',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Trámites', callback_data='tramites')],
            [InlineKeyboardButton(text='📚 Bibliografía', callback_data='bibliografia')],
            [InlineKeyboardButton(text='🏫🚌 ¿Cómo llego?', callback_data='ubicacion')]
        ])
    )


def tramites(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Tramites y formularios:'
        '\nhttps://www.frh.utn.edu.ar/tramitesyformularios/'
        '\nEn caso de necesitar mas información puede consultar el siguiente e-mail sdfasdf@gmail.com',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Volver al principio', callback_data = 'reinicio')]
        ])
    )

def bibliografia(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Aca va el link al drive donde está la bibliografía',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Volver al principio', callback_data = 'reinicio')]
        ])
    )

def ubicacion(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Aca se pone el link al archivo pdf o se pone directamente el archivo, a decidir',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Volver al principio', callback_data = 'reinicio')]
        ])
    )


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.environ['TOKEN'], use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ayuda", start))

    dispatcher.add_handler(CallbackQueryHandler(pattern='reinicio', callback=reinicio))
    dispatcher.add_handler(CallbackQueryHandler(pattern='tramites', callback=tramites))
    dispatcher.add_handler(CallbackQueryHandler(pattern='bibliografia', callback=bibliografia))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ubicacion', callback=ubicacion))



    # Start the Bot
    updater.start_polling()

    print("Bot is polling")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()