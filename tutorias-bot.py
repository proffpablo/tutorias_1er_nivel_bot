import logging
import os
from telegram import Update, ForceReply, message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

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

    user = update.effective_user

    context.bot.send_message(
        chat_id = ID,
        text = fr'Hola {user.mention_markdown_v2()}\!',
    )
    context.bot.send_message(
        chat_id = ID,
        text = 'Te puedo ayudar con lo siguiente: \n/tramites \n/informacion'
    )

def ejemplo_1(update, context):
    update.message.reply_text('Tramites y formularios:\n https://www.frh.utn.edu.ar/tramitesyformularios/ \n en caso de necesitar contactate al sig. email sdfasdf@gmail.com')
    
def ejemplo_2(update, context):
    update.message.reply_text('Información')

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.environ['TOKEN'], use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tramites", ejemplo_1))
    dispatcher.add_handler(CommandHandler("informacion", ejemplo_2))
    dispatcher.add_handler(CommandHandler("ayuda", start))

    # Start the Bot
    updater.start_polling()

    print("Bot is polling")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()