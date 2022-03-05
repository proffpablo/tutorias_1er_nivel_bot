from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ChatAction, ParseMode, replymarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, Filters, MessageHandler

class Bienvenida():
    def send_async(context, *args, **kwargs):
        context.bot.send_message(*args, **kwargs)

    def welcome(update, context, new_member):
        """ Welcomes a user to the chat """

        message = update.message
        chat_id = message.chat.id

        # Mensaje con boton
        message.reply_text(
            text = 'Hola, te doy la bienvenida a ' + message.chat.title + ', contamos un asistente de guiado digital para las dudas'
            ' mas frecuentes, para acceder a él da click en el siguiente boton:',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text = "👉Asistente de Guiado Digital (GUIDI)👈", url = "t.me/tutoria_1er_nivel_bot")]
            ])
        )
        
        # Mensaje sin boton
        """ text = ("Hola $username este es el grupo de Tutorías para 1er año."
        "\nTe recomiendo iniciar el bot dando click aquí: "
        "\n👉\t@tutoria_1er_nivel_bot\t👈"
        "\nEn él podrás responder la mayoría de tus dudas con respecto"
        " a la facultad y la cursada.")

        # Replace placeholders and send message
        text = text.replace("$username", new_member.first_name)
        text = text.replace("$title", message.chat.title)
        Bienvenida.send_async(context, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML) """

    def goodbye(update, context):
        """ Sends goodbye message when a user left the chat """

        message = update.message
        chat_id = message.chat.id

        text = "Adios, $username!"

        # Replace placeholders and send message
        text = text.replace("$username", message.left_chat_member.first_name)
        text = text.replace("$title", message.chat.title)
        Bienvenida.send_async(context, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

    def empty_message(update, context):
        """
        Empty messages could be status messages, so we check them if there is a new
        group member, someone left the chat or if the bot has been added somewhere.
        """
        if update.message.new_chat_members:
            for new_member in update.message.new_chat_members:
                return Bienvenida.welcome(update, context, new_member)

        # Someone left the chat
        elif update.message.left_chat_member is not None:
            return Bienvenida.goodbye(update, context)