import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ChatAction, ParseMode, replymarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, Filters, MessageHandler
import mensaje_bienvenida

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Variables anuales
calendario_academico = "https://www.frh.utn.edu.ar/media/calendario_academico/2021/12/29/calendario_2022.pdf"

# Menú principal.
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
            [InlineKeyboardButton(text='Seminario de Ingreso', callback_data = 'ingreso')],
            [InlineKeyboardButton(text='Primer año', callback_data = 'primero')],
            [InlineKeyboardButton(text='Años superiores', callback_data = 'superiores')],
            [InlineKeyboardButton(text='Graduados', callback_data = 'graduados')],
        ])
    )

def reinicio(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Selecciona una opción:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Seminario de Ingreso', callback_data = 'ingreso')],
            [InlineKeyboardButton(text='Primer año', callback_data = 'primero')],
            [InlineKeyboardButton(text='Años superiores', callback_data = 'superiores')],
            [InlineKeyboardButton(text='Graduados', callback_data = 'graduados')],
        ])
    )

"""def bibliografia(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = 'En este drive encontraran bibliografía útil para cada carrera:'
        '\nhttps://drive.google.com/drive/u/0/folders/1M7VwEvSmzE7v5t1jfd8N5LxdV8SIscbR',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='🔙 Volver', callback_data = 'first')],
        ])
    )
"""

#Ingreso
def ingreso(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Selecciona una opción:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Administrativo', callback_data = 'ing_adm')],
            [InlineKeyboardButton(text='Académico', callback_data = 'ing_acad')],
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'reinicio')],
        ])
    )

def administrativo(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Selecciona una opción:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Cuanto dura el ingreso y fechas de examen', callback_data = 'ing_calendario')],
            [InlineKeyboardButton(text='Debo certificar que curso el ingreso', callback_data = 'ing_cons_cur')],
            [InlineKeyboardButton(text='¿Necesitas cambiarte de turno?', callback_data = 'ing_comision')],
            [InlineKeyboardButton(text='¿Rendiste examén y pediste el día en el trabajo?', callback_data = 'ing_cons_ex')],
            [InlineKeyboardButton(text='Necesitas comunicarte con tu tutor por otro motivo', callback_data = 'ing_tutores')],
            [InlineKeyboardButton(text='Aprobaste el ingreso y queres cambiarte de regional', callback_data = 'ing__adm')],
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ingreso')],
        ])
    )

def ing_calendario(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Esa información la encontrarás en el calendario académico:"
        "\n" + calendario_academico,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_adm')],
        ])
    )

def constancia_cursado(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Link a un pdf para descargar la constancia de cursado",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_adm')],
        ])
    )

def cambio_comision(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Formulario para cambio de comisión",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_adm')],
        ])
    )

def constancia_examen(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Link a un pdf para descargar la constancia de examen",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_adm')],
        ])
    )

def contacto_tutores(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Poner contacto de los tutores por comisión",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_adm')],
        ])
    )

def contancia_ingreso_aprobado(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Instructivo de como solicitar la constancia de ingreso aprobado",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_adm')],
        ])
    )

def academico(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Selecciona una opción:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='¿Conoces que se ve en el ingreso?', callback_data = 'ing_contenidos')],
            [InlineKeyboardButton(text='Condiciones de aprobación', callback_data = 'ing_cond_ap')],
            [InlineKeyboardButton(text='¿Necesitas la guía de ejercicios o material de estudio?', callback_data = 'ing_material')],
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ingreso')],
        ])
    )

def contenidos(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Contenidos",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_acad')],
        ])
    )

def condiciones_aprobacion(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Selecciona una opción:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Matemática', callback_data = 'ing_cond_mate')],
            [InlineKeyboardButton(text='Física', callback_data = 'ing_cond_fis')],
            [InlineKeyboardButton(text='Introducción a la universidad', callback_data = 'ing_cond_intro')],
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_acad')],
        ])
    )

def condiciones_matematica(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Condiciones de aprobación de matemática",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_cond_ap')],
        ])
    )

def condiciones_fisica(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Condiciones de aprobación de física",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_cond_ap')],
        ])
    )

def condiciones_introduccion(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text = "Condiciones de aprobación de introducción a la universidad1",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_cond_ap')],
        ])
    )

def material(update, context):
        query = update.callback_query
        query.answer()

        query.edit_message_text(
            text = "Selecciona una opción:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Matemática', callback_data = 'ing_mat_mate')],
                [InlineKeyboardButton(text='Física', callback_data = 'ing_mat_fis')],
                [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_acad')],
            ])
        )

def material_matematica(update, context):
        query = update.callback_query
        query.answer()

        query.edit_message_text(
            text = "Te dejamos un drive donde vas a encontrar la guía de matemática y ejercicios "
            "\nhttps://drive.google.com/drive/folders/1RCToq5TkZ14wfGUhIl_TTmnj7WZRFhD1?usp=sharing",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_material')],
            ])
        )

def material_fisica(update, context):
        query = update.callback_query
        query.answer()

        query.edit_message_text(
            text = "Te dejamos un drive donde vas a encontrar la guía de física y ejercicios "
            "\nhttps://drive.google.com/drive/folders/1ZIRl-7JseeE0b3wdvWbSJm2yUBhzqGbX",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='🔙 Volver', callback_data = 'ing_material')],
            ])
        )

def main() -> None:
    # Se añade el token a través de una variable de entorno.
    updater = Updater(os.environ['TOKEN'], use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Comandos para iniciar con el bot.
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("bot", start))
    dispatcher.add_handler(CallbackQueryHandler(pattern = 'reinicio', callback = reinicio))

    # Mensaje de bienvenida.
    bienvenida = mensaje_bienvenida.Bienvenida
    dispatcher.add_handler(MessageHandler(Filters.status_update, bienvenida.empty_message))

    # Seminario de ingreso.
    dispatcher.add_handler(CallbackQueryHandler(pattern='ingreso', callback = ingreso))

    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_adm', callback = administrativo))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_calendario', callback = ing_calendario))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_cons_cur', callback = constancia_cursado))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_comision', callback = cambio_comision))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_cons_ex', callback = constancia_examen))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_tutores', callback = contacto_tutores))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing__adm', callback = contancia_ingreso_aprobado))

    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_acad', callback = academico))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_contenidos', callback = contenidos))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_cond_ap', callback = condiciones_aprobacion))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_cond_mate', callback = condiciones_matematica))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_cond_fis', callback = condiciones_fisica))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_cond_intro', callback = condiciones_introduccion))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_material', callback = material))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_mat_mate', callback = material_matematica))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ing_mat_fis', callback = material_fisica))


    # Inicia el bot.
    updater.start_polling()
    print("Bot iniciado")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.

if __name__ == '__main__':
    main()
