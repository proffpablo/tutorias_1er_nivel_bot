import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ChatAction, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, Filters, MessageHandler
from telegram.ext.dispatcher import run_async
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Mensaje de bienvenida.
def send_async(context, *args, **kwargs):
    context.bot.send_message(*args, **kwargs)

def welcome(update, context, new_member):
    """ Welcomes a user to the chat """

    message = update.message
    chat_id = message.chat.id

    text = ("Hola $username este es el grupo de Tutorías para 1er año."
    "\nTe recomiendo iniciar el bot dando click aquí: "
    "\n👉\t@tutoria_1er_nivel_bot\t👈"
    "\nEn él podrás responder la mayoría de tus dudas con respecto"
    " a la facultad y la cursada.")

    # Replace placeholders and send message
    text = text.replace("$username", new_member.first_name)
    text = text.replace("$title", message.chat.title)
    send_async(context, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

def goodbye(update, context):
    """ Sends goodbye message when a user left the chat """

    message = update.message
    chat_id = message.chat.id

    text = "Adios, $username!"

    # Replace placeholders and send message
    text = text.replace("$username", message.left_chat_member.first_name)
    text = text.replace("$title", message.chat.title)
    send_async(context, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

def empty_message(update, context):
    """
    Empty messages could be status messages, so we check them if there is a new
    group member, someone left the chat or if the bot has been added somewhere.
    """
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            return welcome(update, context, new_member)

    # Someone left the chat
    elif update.message.left_chat_member is not None:
        return goodbye(update, context)

# Botones y contenido.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    ID = update.message.from_user.id

    update.message.chat.send_action(
        action=ChatAction.TYPING,
        timeout=None
    )

    context.bot.send_message(
        chat_id = ID,
        text = 'Hola, selecciona una opción:',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🏃🏃‍♀️ Aspirante(Seminario de ingreso)', callback_data='ingreso')],
            [InlineKeyboardButton(text='🙋‍♂️🙋 General', callback_data='first')],
        ])
    )

def reinicio(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Selecciona una opción:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🏃🏃‍♀️ Ingreso', callback_data='ingreso')],
            [InlineKeyboardButton(text='🙋‍♂️🙋 1er año', callback_data='first')],
            [InlineKeyboardButton(text='👨‍🎓👩‍🎓 Avanzado', callback_data='avanzado')],
        ])
    )

def ingreso(update, context):
    query = update.callback_query
    query.answer()

def first(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Te puedo ayudar en lo siguiente:',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='📋 Trámites', callback_data='tramites')],
            [InlineKeyboardButton(text='📚 Bibliografía', callback_data='bibliografia')],
            [InlineKeyboardButton(text='🧭 ¿Cómo llego?', callback_data='ubicacion')],
            [InlineKeyboardButton(text='🗓️ Calendario académico', callback_data='calendario')],
            [InlineKeyboardButton(text='⚤ Comisión de género', callback_data='genero')],
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'reinicio')],
        ])
    )

def avanzado(update, context):
    query = update.callback_query
    query.answer()

def tramites(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Tramites y formularios:'
        '\nhttps://www.frh.utn.edu.ar/tramitesyformularios/'
        '\nEn caso de necesitar mas información puede '
        'consultar el siguiente e-mail sdfasdf@gmail.com',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='🔙 Volver', callback_data = 'first')],
        ])
    )

def bibliografia(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'En este drive encontraran bibliografía útil para cada carrera:'
        '\nhttps://drive.google.com/drive/u/0/folders/1M7VwEvSmzE7v5t1jfd8N5LxdV8SIscbR',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='🔙 Volver', callback_data = 'first')],
        ])
    )

def ubicacion(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Para ir a la UTN FRH, ubicada en París 532, Haedo, Provincia de Buenos Aires, uno tiene varios medios a su '
        'disposición para llegar por su excelente posicionamiento geográfico, te mencionaremos algunas formas para que puedas venir.',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='🚗 Auto', callback_data = 'auto')],
        [InlineKeyboardButton(text='🚌 Transporte público', callback_data = 'bus')],
        [InlineKeyboardButton(text='🔙 Volver', callback_data = 'first')],
        ])
    )

def ubicacion_auto(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Si contas con un vehículo propio, el establecimiento se encuentra cerca de vías principales'
        ' como el Acceso Oeste, Av. Gaona o Av. Rivadavia. La universidad posee un estacionamiento propio donde dejar'
        ' los vehículos tanto del personal como de los estudiantes de esta. ',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='🔍 Apps útiles', callback_data = 'app_auto')],
        [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ubicacion')],

        ])
    )

def app_auto(update, context):
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
        [InlineKeyboardButton(text='🔙 Volver', callback_data = 'first')],
        ])
    )

def genero(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'Si sufrís o sentís alguna situación de violencia o que te genere incomodidad'
        'dentro del hámbito facultativo podemos orienterte y acompañarte.'
        ' Escribí a comisiondegenero@frh.utn.edu.ar',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='🔙 Volver', callback_data = 'first')],
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

    dispatcher.add_handler(CallbackQueryHandler(pattern='ingreso', callback=ingreso))
    dispatcher.add_handler(CallbackQueryHandler(pattern='avanzado', callback=avanzado))
    dispatcher.add_handler(CallbackQueryHandler(pattern='first', callback=first))
    dispatcher.add_handler(CallbackQueryHandler(pattern='reinicio', callback=reinicio))
    dispatcher.add_handler(CallbackQueryHandler(pattern='tramites', callback=tramites))
    dispatcher.add_handler(CallbackQueryHandler(pattern='bibliografia', callback=bibliografia))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ubicacion', callback=ubicacion))
    dispatcher.add_handler(CallbackQueryHandler(pattern='calendario', callback=calendario))
    dispatcher.add_handler(CallbackQueryHandler(pattern='auto', callback=ubicacion_auto))
    dispatcher.add_handler(CallbackQueryHandler(pattern='auto', callback=ubicacion_auto))
    dispatcher.add_handler(CallbackQueryHandler(pattern='bus', callback=app_auto))
    dispatcher.add_handler(CallbackQueryHandler(pattern='genero', callback=genero))

    dispatcher.add_handler(MessageHandler(Filters.status_update, empty_message))

    # Start the Bot
    updater.start_polling()

    print("Bot is polling")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
