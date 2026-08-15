import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

TOKEN = "8654409228:AAFbp0ywyahBzC_OEFR7djyFiUETv_7LzwE"

# Tu ID de Telegram.
# Solo tú podrás utilizar la función para obtener file_id.
ADMIN_ID = 8800247127


# ==========================================================
# LOGS
# ==========================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# ==========================================================
# CONTENIDO
#
# IMPORTANTE:
# Cada día tiene un número diferente.
#
# DÍA 1 = 001
# DÍA 2 = 002
# DÍA 3 = 003
#
# NUNCA MODIFIQUES UN DÍA QUE YA PUBLICASTE.
# ==========================================================

CONTENIDO = {


    # ======================================================
    # DÍA 1
    # Ejemplo: aquí puedes poner 16 vídeos
    # Enlace:
    # https://t.me/snufy_bot?start=001
    # ======================================================

    "001": [

        {
            "file_id": "BAACAgIAAxkBAAICGGqA0ixxrRuu27HoKhAe1c-R2HL0AAJBSgAC_jYxSaf8mghoKpnmPQQ",
            "caption": "🎬 Vídeo 1"
        },


        # Puedes seguir agregando todos los vídeos que quieras.


    ],


    # ======================================================
    # DÍA 2
    # Aquí tú decides cuántos vídeos poner.
    #
    # Enlace:
    # https://t.me/snufy_bot?start=002
    # ======================================================

    "002": [

        {
            "file_id": "FILE_ID_VIDEO_1",
            "caption": "🎬 Vídeo 1"
        },

        {
            "file_id": "FILE_ID_VIDEO_2",
            "caption": "🎬 Vídeo 2"
        },

        {
            "file_id": "FILE_ID_VIDEO_3",
            "caption": "🎬 Vídeo 3"
        }


    ],


    # ======================================================
    # DÍA 3
    # Aquí también puedes poner la cantidad que quieras.
    #
    # Enlace:
    # https://t.me/snufy_bot?start=003
    # ======================================================

    "003": [

        {
            "file_id": "FILE_ID_VIDEO_1",
            "caption": "🎬 Vídeo 1"
        }


    ],


    # ======================================================
    # DÍA 4
    #
    # Cuando llegue el día 4, agrega aquí los vídeos.
    #
    # Enlace:
    # https://t.me/snufy_bot?start=004
    # ======================================================

    "004": [

        {
            "file_id": "FILE_ID_VIDEO_1",
            "caption": "🎬 Vídeo 1"
        }


    ]

}


# ==========================================================
# COMANDO /START
# ==========================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # Comprobar si existe un código después de /start

    if not context.args:

        await update.message.reply_text(
            "👋 ¡Hola!\n\n"
            "Para recibir el contenido, utiliza uno de "
            "los enlaces publicados en nuestro canal."
        )

        return


    # Obtener el código

    codigo = context.args[0].lower()


    # Comprobar que el código existe

    if codigo not in CONTENIDO:

        await update.message.reply_text(
            "⚠️ El enlace utilizado no es válido "
            "o ha caducado."
        )

        return


    # Obtener los vídeos de ese día

    videos = CONTENIDO[codigo]

    total = len(videos)


    # Avisar al usuario

    await update.message.reply_text(
        f"🎁 ¡Regalo encontrado!\n\n"
        f"🎬 Te estoy enviando {total} vídeo(s)..."
    )


    # Enviar todos los vídeos

    for video in videos:

        try:

            await context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=video["file_id"],
                caption=video["caption"]
            )

        except Exception as error:

            logging.error(
                f"Error enviando video: {error}"
            )

            await update.message.reply_text(
                "❌ No se pudo enviar uno de los vídeos."
            )


# ==========================================================
# OBTENER FILE_ID DE UN VIDEO
# ==========================================================

async def recibir_video(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # Solo el administrador puede usar esta función

    if update.effective_user.id != ADMIN_ID:
        return


    # Obtener información del vídeo

    video = update.message.video

    file_id = video.file_id


    # Mostrar file_id

    await update.message.reply_text(
        "🎬 FILE ID OBTENIDO\n\n"
        f"{file_id}\n\n"
        "📌 Copia este ID y colócalo en el día correspondiente."
    )


    logging.info(
        f"Nuevo file_id obtenido: {file_id}"
    )


# ==========================================================
# COMANDO /ID
# ==========================================================

async def id_usuario(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        f"🆔 Tu ID de Telegram es:\n\n"
        f"{update.effective_user.id}"
    )


# ==========================================================
# INICIAR BOT
# ==========================================================

if __name__ == "__main__":

    print("======================================")
    print("BOT DE REGALOS - VERSION 4.0")
    print("======================================")

    app = ApplicationBuilder().token(TOKEN).build()


    # Comando /start

    app.add_handler(
        CommandHandler("start", start)
    )


    # Comando /id

    app.add_handler(
        CommandHandler("id", id_usuario)
    )


    # Detectar vídeos enviados al bot

    app.add_handler(
        MessageHandler(
            filters.VIDEO,
            recibir_video
        )
    )


    print("Bot iniciado correctamente.")

    app.run_polling()