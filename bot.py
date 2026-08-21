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

# Tu ID de Telegram
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
# Cada día tiene su propio enlace.
#
# DÍA 1 → ?start=001
# DÍA 2 → ?start=002
# DÍA 3 → ?start=003
# ...
# DÍA 10 → ?start=010
#
# IMPORTANTE:
# Nunca cambies un día que ya hayas publicado.
# ==========================================================

CONTENIDO = {

    # ======================================================
    # DÍA 1
    # https://t.me/snufy_bot?start=001
    # ======================================================

    "001": [

        {
            "file_id": "BAACAgIAAxkBAAICGGqA0ixxrRuu27HoKhAe1c-R2HL0AAJBSgAC_jYxSaf8mghoKpnmPQQ",
            "caption": "🎬 Vídeo 1"
        }

    ],


    # ======================================================
    # DÍA 2
    # https://t.me/snufy_bot?start=002
    # ======================================================

    "002": [

        {
            "file_id": "BAACAgEAAxkBAAMraoAFG61oAStiZOfWSa2IXY2G2zYAAisJAAKO9BlH71eGqGld_x89BA",
            "caption": "🎬 Vídeo 1"
        }

    ],


    # ======================================================
    # DÍA 3
    # https://t.me/snufy_bot?start=003
    # ======================================================

    "003": [

    {
        "file_id": "BAACAgEAAxkBAAIDM2qBwWRx2X2LEgWQ_es8my2vK99mAALSCAACFXj4Re_xIfILT3BiPQQ",
        "caption": "🎬 Vídeo 1"
    },

    {
        "file_id": "BAACAgIAAxkBAAIDNWqBwY_3dTIhdh0gtyhhcZAKyBRyAAJ3ggAC2WJhSsx_uMJxLF-5PQQ",
        "caption": "🎬 Vídeo 2"
    },

    {
        "file_id": "BAACAgEAAxkBAAIDN2qBwbFEvwFj3PzqVGOMOtCNyiolAAKBCAACFXj4RVY7fTj9RefJPQQ",
        "caption": "🎬 Vídeo 3"
    },

],

    # ======================================================
    # DÍA 4
    # https://t.me/snufy_bot?start=004
    # ======================================================

    "004": [

     {
        "file_id": "BAACAgEAAxkBAAIDyWqCHywvQvTPejwjop8mwQncLAlaAAJkBQACSp4YRGDmrkypVWtDPQQ",
        "caption": "🎬 Vídeo 1"
    },

    {
        "file_id": "BAACAgUAAxkBAAIDy2qCH_z_h2B9sa-6Nn7KPhYCa2tXAAImHwACOnf5VTEesaKGZbSmPQQ",
        "caption": "🎬 Vídeo 2"
    },

],


    # ======================================================
    # DÍA 5
    # https://t.me/snufy_bot?start=005
    # ======================================================

    "005": [

    {
        "file_id": "BAACAgIAAxkBAAIE5WqDXKow-z3dH5j6k_30V3chNht9AAIVQAACvbOASjRVlt7EDZDkPQQ",
        "caption": "🎬 Vídeo 1"
    },

    {
        "file_id": "BAACAgEAAxkBAAIE52qDXP8KfAF9l7FWqwiFY8gFg_2cAAK2BgACi1rJRWYq2DUKOWmWPQQ",
        "caption": "🎬 Vídeo 2"
    },

    {
        "file_id": "BAACAgIAAxkBAAIE6WqDXSCVh48hRC4hl8iHwxHYDi4yAAIcXAACHrbhSLS6ZSKoJT77PQQ",
        "caption": "🎬 Vídeo 3"
    },

],


    # ======================================================
    # DÍA 6
    # https://t.me/snufy_bot?start=006
    # ======================================================

    "006": [

    {
        "file_id": "BAACAgEAAxkBAAIHc2qF6Swd03E3HY9wXcDbfByxgrBUAAIkBwACa-MJRVCdkOpFaNNjPQQ",
        "caption": "🎬 Vídeo 1"
    },
            
    {
        "file_id": "BAACAgEAAxkBAAIHdWqF6UO5sP6B8gPdXS2ybKn3wNpSAAKQBwAC81kxRX40CUB30ZgyPQQ",
        "caption": "🎬 Vídeo 2"
    },

    {
        "file_id": "BAACAgQAAxkBAAIHeGqF6fBMAAG_GMDLrmeoT22rV68vhwACsSEAAq3r8VHHtoe1Zy6_0z0E",
        "caption": "🎬 Vídeo 3"
    },

    {
        "file_id": "BAACAgQAAxkBAAIHemqF6g2E2DaWSJ5KaqtWbA0ST10OAAKyIQACrevxUR2NKvoueUvmPQQ",
        "caption": "🎬 Vídeo 4"
    },
    
    {
        "file_id": "BAACAgEAAxkBAAIHfGqF6jSE5fBuvBgu9W9ktBbCNYxZAALNBwACk5AJRj-3-n7MZv3XPQQ",
        "caption": "🎬 Vídeo 5"
    },

    {
        "file_id": "BAACAgEAAxkBAAIHfmqF6klWRAQWqdrv6pthEVYUPARRAAIZCAACk5AJRqNSuuwHlWEoPQQ",
        "caption": "🎬 Vídeo 6"
    },

    {
        "file_id": "BAACAgEAAxkBAAIHgGqF6mOkTr-Ynw8umLNXRqkfThhQAAJ4CAAC35cQRtvuwjsiPj3fPQQ",
        "caption": "🎬 Vídeo 7"
    },

],


    # ======================================================
    # DÍA 7
    # https://t.me/snufy_bot?start=007
    # ======================================================

    "007": [

        {
            "file_id": "BAACAgEAAxkBAAIJ12qHIv7GJYY4yo9Qi8-Q_x8-Xrd6AAKRBQAC9uiJRH5RXzJkil0wPQQ",
            "caption": "🎬 Vídeo 1"
        },
        
        {
            "file_id": "BAACAgEAAxkBAAIJ2WqHI4Uh6AfwoBjEK08XZqOkIiKtAAIHCgAC1_JZR2CJzsDpdulmPQQ",
            "caption": "🎬 Vídeo 1"
        },

    ],


    # ======================================================
    # DÍA 8
    # https://t.me/snufy_bot?start=008
    # ======================================================

    "008": [

        {
            "file_id": "BAACAgEAAxkBAAIM3WqH7z2cW2U8Ubg7OfligmeUzdy0AAI9BwACHHc5REnVCk_GSOquPQQ",
            "caption": "🎬 Vídeo 1"
        },
              
        {
            "file_id": "BAACAgEAAxkBAAIM32qH74rfyQPD8MHE6TgKUUa51JFTAAIMBwACzcvRR7nMTIcfvR7DPQQ",
            "caption": "🎬 Vídeo 2"
        },
      
        {
            "file_id": "BAACAgUAAxkBAAIM4WqH77k5IOlPuWgLghSu9duaOpsuAAKbIAACMmyAV-Wpf6hsP0AePQQ",
            "caption": "🎬 Vídeo 3"
        },
        
        {
            "file_id": "BAACAgEAAxkBAAIM42qH791bvwfAt_LB38T22LTJ27bRAAKwCAACOguxR5bFIelvKsBfPQQ",
            "caption": "🎬 Vídeo 4"
        },
        
        {
            "file_id": "BAACAgEAAxkBAAIM5WqH8GOLT5gr5z47LglLJ4IQcz2jAAL1BwACOuLhR0L3QYZArLK6PQQ",
            "caption": "🎬 Vídeo 5"
        },
        
        {
            "file_id": "BAACAgEAAxkBAAIM52qH8Ibl1_-znh3BMhK1Fh7-DUtuAALXCgACEBxJRfhuH1KzQCAkPQQ",
            "caption": "🎬 Vídeo 6"
        },
        
        {
            "file_id": "BAACAgIAAxkBAAIM6WqH8LzSAbK4I9c39uIO2YCTXTVtAAJjpAACxBDZSy5nNKKG83eIPQQ",
            "caption": "🎬 Vídeo 7"
        },      
        
        {
            "file_id": "BAACAgIAAxkBAAIM62qH8WrxrrZDA1vvDI_Ej-l1Ki7qAAK3owACfwGoSnyY87xuzlTIPQQ",
            "caption": "🎬 Vídeo 8"
        },
        
        {
            "file_id": "BAACAgEAAxkBAAIM7WqH8ag8eYI9WXm_W81TWGbMQ8x8AAI4BwACHHc5ROYsCMQC80JUPQQ",
            "caption": "🎬 Vídeo 9"
        },
        
        {
            "file_id": "BAACAgEAAxkBAAIM72qH8b6RJCmenbLE0S5UOI9h8VR4AAI6BwACHHc5RCz2B-GzFjC0PQQ",
            "caption": "🎬 Vídeo 10"
        },
  
    ],
    


    # ======================================================
    # DÍA 9
    # https://t.me/snufy_bot?start=009
    # ======================================================

    "009": [

        {
            "file_id": "FILE_ID_AQUI",
            "caption": "🎬 Vídeo 1"
        }

    ],


    # ======================================================
    # DÍA 10
    # https://t.me/snufy_bot?start=010
    # ======================================================

    "010": [

        {
            "file_id": "FILE_ID_AQUI",
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

    if not context.args:

        await update.message.reply_text(
            "👋 ¡Hola!\n\n"
            "Para recibir el contenido, utiliza uno de "
            "los enlaces publicados en nuestro canal."
        )

        return


    # Obtener el código del enlace

    codigo = context.args[0].lower()


    # Comprobar si existe

    if codigo not in CONTENIDO:

        await update.message.reply_text(
            "⚠️ El enlace utilizado no es válido "
            "o ha caducado."
        )

        return


    # Obtener los videos

    videos = CONTENIDO[codigo]

    total = len(videos)


    # Avisar al usuario

    await update.message.reply_text(
        f"🎁 ¡Regalo encontrado!\n\n"
        f"🎬 Te estoy enviando {total} vídeo(s)..."
    )


    # Enviar todos los videos del día

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
# OBTENER FILE_ID
# ==========================================================

async def recibir_video(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # Solo el administrador puede obtener file_id

    if update.effective_user.id != ADMIN_ID:
        return


    video = update.message.video

    file_id = video.file_id


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


    # /start

    app.add_handler(
        CommandHandler("start", start)
    )


    # /id

    app.add_handler(
        CommandHandler("id", id_usuario)
    )


    # Recibir videos y obtener file_id

    app.add_handler(
        MessageHandler(
            filters.VIDEO,
            recibir_video
        )
    )


    print("Bot iniciado correctamente.")

    app.run_polling()