import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)


# ============================================================
# CONFIGURACIÓN
# ============================================================

TOKEN = "8654409228:AAFbp0ywyahBzC_OEFR7djyFiUETv_7LzwE"

# Tu ID de Telegram.
# Lo puedes obtener temporalmente con un bot como @userinfobot.
# Pon aquí solamente TU ID para que nadie más pueda obtener file_id.
ADMIN_ID = 8800247127


# ============================================================
# LOGS
# ============================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# ============================================================
# MIXTAPES
# ============================================================

MIXTAPES = {

    "mixtape1": [
        {
            "file_id": "BAACAgEAAxkBAAMraoAFG61oAStiZOfWSa2IXY2G2zYAAisJAAKO9BlH71eGqGld_x89BA",
            "caption": "🎬 Vídeo 1 de 1"
        }
    ],

    "mixtape2": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 2"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 2"
        }
    ],

    "mixtape3": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 3"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 3"
        },
        {
            "file_id": "FILE_ID_3",
            "caption": "🎬 Vídeo 3 de 3"
        }
    ],

    "mixtape4": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 4"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 4"
        },
        {
            "file_id": "FILE_ID_3",
            "caption": "🎬 Vídeo 3 de 4"
        },
        {
            "file_id": "FILE_ID_4",
            "caption": "🎬 Vídeo 4 de 4"
        }
    ],

    "mixtape5": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 5"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 5"
        },
        {
            "file_id": "FILE_ID_3",
            "caption": "🎬 Vídeo 3 de 5"
        },
        {
            "file_id": "FILE_ID_4",
            "caption": "🎬 Vídeo 4 de 5"
        },
        {
            "file_id": "FILE_ID_5",
            "caption": "🎬 Vídeo 5 de 5"
        }
    ],

    "mixtape6": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 6"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 6"
        },
        {
            "file_id": "FILE_ID_3",
            "caption": "🎬 Vídeo 3 de 6"
        },
        {
            "file_id": "FILE_ID_4",
            "caption": "🎬 Vídeo 4 de 6"
        },
        {
            "file_id": "FILE_ID_5",
            "caption": "🎬 Vídeo 5 de 6"
        },
        {
            "file_id": "FILE_ID_6",
            "caption": "🎬 Vídeo 6 de 6"
        }
    ],

    "mixtape7": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 7"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 7"
        },
        {
            "file_id": "FILE_ID_3",
            "caption": "🎬 Vídeo 3 de 7"
        },
        {
            "file_id": "FILE_ID_4",
            "caption": "🎬 Vídeo 4 de 7"
        },
        {
            "file_id": "FILE_ID_5",
            "caption": "🎬 Vídeo 5 de 7"
        },
        {
            "file_id": "FILE_ID_6",
            "caption": "🎬 Vídeo 6 de 7"
        },
        {
            "file_id": "FILE_ID_7",
            "caption": "🎬 Vídeo 7 de 7"
        }
    ],

    "mixtape8": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 8"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 8"
        },
        {
            "file_id": "FILE_ID_3",
            "caption": "🎬 Vídeo 3 de 8"
        },
        {
            "file_id": "FILE_ID_4",
            "caption": "🎬 Vídeo 4 de 8"
        },
        {
            "file_id": "FILE_ID_5",
            "caption": "🎬 Vídeo 5 de 8"
        },
        {
            "file_id": "FILE_ID_6",
            "caption": "🎬 Vídeo 6 de 8"
        },
        {
            "file_id": "FILE_ID_7",
            "caption": "🎬 Vídeo 7 de 8"
        },
        {
            "file_id": "FILE_ID_8",
            "caption": "🎬 Vídeo 8 de 8"
        }
    ],

    "mixtape9": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 9"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 9"
        },
        {
            "file_id": "FILE_ID_3",
            "caption": "🎬 Vídeo 3 de 9"
        },
        {
            "file_id": "FILE_ID_4",
            "caption": "🎬 Vídeo 4 de 9"
        },
        {
            "file_id": "FILE_ID_5",
            "caption": "🎬 Vídeo 5 de 9"
        },
        {
            "file_id": "FILE_ID_6",
            "caption": "🎬 Vídeo 6 de 9"
        },
        {
            "file_id": "FILE_ID_7",
            "caption": "🎬 Vídeo 7 de 9"
        },
        {
            "file_id": "FILE_ID_8",
            "caption": "🎬 Vídeo 8 de 9"
        },
        {
            "file_id": "FILE_ID_9",
            "caption": "🎬 Vídeo 9 de 9"
        }
    ],

    "mixtape10": [
        {
            "file_id": "FILE_ID_1",
            "caption": "🎬 Vídeo 1 de 10"
        },
        {
            "file_id": "FILE_ID_2",
            "caption": "🎬 Vídeo 2 de 10"
        },
        {
            "file_id": "FILE_ID_3",
            "caption": "🎬 Vídeo 3 de 10"
        },
        {
            "file_id": "FILE_ID_4",
            "caption": "🎬 Vídeo 4 de 10"
        },
        {
            "file_id": "FILE_ID_5",
            "caption": "🎬 Vídeo 5 de 10"
        },
        {
            "file_id": "FILE_ID_6",
            "caption": "🎬 Vídeo 6 de 10"
        },
        {
            "file_id": "FILE_ID_7",
            "caption": "🎬 Vídeo 7 de 10"
        },
        {
            "file_id": "FILE_ID_8",
            "caption": "🎬 Vídeo 8 de 10"
        },
        {
            "file_id": "FILE_ID_9",
            "caption": "🎬 Vídeo 9 de 10"
        },
        {
            "file_id": "FILE_ID_10",
            "caption": "🎬 Vídeo 10 de 10"
        }
    ]
}


# ============================================================
# COMANDO /START
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    args = context.args

    if not args:
        await update.message.reply_text(
            "👋 ¡Hola!\n\n"
            "Para recibir contenido, utiliza uno de los enlaces "
            "proporcionados por nuestro canal."
        )
        return

    clave = args[0].lower()

    if clave not in MIXTAPES:
        await update.message.reply_text(
            "⚠️ El enlace utilizado no es válido o ha caducado."
        )
        return

    lista_videos = MIXTAPES[clave]

    await update.message.reply_text(
        f"🎬 ¡Hola!\n\n"
        f"Te estoy enviando {len(lista_videos)} vídeo(s)..."
    )

    for video in lista_videos:

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


# ============================================================
# OBTENER FILE_ID
# ============================================================

async def recibir_video(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Solo el administrador puede utilizar esta función
    if update.effective_user.id != ADMIN_ID:
        return

    video = update.message.video

    file_id = video.file_id

    await update.message.reply_text(
        "🎬 FILE ID OBTENIDO\n\n"
        f"{file_id}\n\n"
        "📌 Copia este ID y colócalo en MIXTAPES."
    )

    logging.info(
        f"Nuevo file_id obtenido: {file_id}"
    )


# ============================================================
# COMANDO /ID
# ============================================================

async def id_usuario(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        f"🆔 Tu ID de Telegram es:\n\n"
        f"{update.effective_user.id}"
    )


# ============================================================
# INICIAR BOT
# ============================================================

if __name__ == "__main__":

    print("======================================")
    print("BOT MIXTAPES - VERSION 2.0")
    print("======================================")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("id", id_usuario)
    )

    app.add_handler(
        MessageHandler(
            filters.VIDEO,
            recibir_video
        )
    )

    print("Bot iniciado correctamente.")

    app.run_polling()