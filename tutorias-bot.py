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
            [InlineKeyboardButton(text='🧭 ¿Cómo llego?', callback_data='ubicacion')],
            [InlineKeyboardButton(text='🗓️ Calendario académico', callback_data='calendario')],
            [InlineKeyboardButton(text='⚤ Comisión de género', callback_data='genero')],           
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
            [InlineKeyboardButton(text='🧭 ¿Cómo llego?', callback_data='ubicacion')],
            [InlineKeyboardButton(text='🗓️ Calendario académico', callback_data='calendario')],
            [InlineKeyboardButton(text='⚤ Comisión de género', callback_data='genero')],
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
        [InlineKeyboardButton(text='Volver al principio', callback_data = 'reinicio')],
        ])
    )

def bibliografia(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'En este drive encontraran bibliografía útil para cada carrera:'
        '\nhttps://drive.google.com/drive/u/0/folders/1M7VwEvSmzE7v5t1jfd8N5LxdV8SIscbR',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Volver al principio', callback_data = 'reinicio')],
        ])
    )

def ubicacion(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Indique tipo de transporte',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='🚗 Auto', callback_data = 'auto')],
        [InlineKeyboardButton(text='🚌 Transporte público', callback_data = 'bus')],
        [InlineKeyboardButton(text='Volver al principio', callback_data = 'reinicio')],
        ])
    )

def ubicacion_auto(update, context):
    query = update.callback_query
    query.answer()

def ubicacion_bus(update, context):
    query = update.callback_query
    query.answer()

def calendario(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Este es el Calendario Académico'
        '\nhttps://www.frh.utn.edu.ar/media/calendario_academico/2021/02/18/calendario.pdf',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Volver al principio', callback_data = 'reinicio')],
        ])
    )

def genero(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Si sufrís o sentís alguna situación de violencia o que te genere incomodidad'
        'dentro del hámbito facultativo podemos orienterte y acompañarte. Escribí a comisiondegenero@frh.utn.edu.ar',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Volver al principio', callback_data = 'reinicio')],
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
    dispatcher.add_handler(CommandHandler("bot", start))

    dispatcher.add_handler(CallbackQueryHandler(pattern='reinicio', callback=reinicio))
    dispatcher.add_handler(CallbackQueryHandler(pattern='tramites', callback=tramites))
    dispatcher.add_handler(CallbackQueryHandler(pattern='bibliografia', callback=bibliografia))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ubicacion', callback=ubicacion))
    dispatcher.add_handler(CallbackQueryHandler(pattern='calendario', callback=calendario))
    dispatcher.add_handler(CallbackQueryHandler(pattern='auto', callback=ubicacion_auto))
    dispatcher.add_handler(CallbackQueryHandler(pattern='bus', callback=ubicacion_bus))
    dispatcher.add_handler(CallbackQueryHandler(pattern='genero', callback=genero))



    # Start the Bot
    updater.start_polling()

    print("Bot is polling")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()