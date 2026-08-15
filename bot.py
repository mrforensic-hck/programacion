import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuración de logs para monitorear en Render
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 1. Tu Token de @BotFather:
TOKEN = "8654409228:AAFbp0ywyahBzC_OEFR7djyFiUETv_7LzwE"

# 2. DICCIONARIO DE MIXTAPES (De 1 a 10 vídeos)
MIXTAPES = {
    # Para enlace: https://t.me/TuBotUsername?start=mixtape1
    "mixtape1": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 1"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape2
    "mixtape2": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 2"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 2"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape3
    "mixtape3": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 3"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 3"},
        {"file_id": "FILE_ID_3", "caption": "🎬 Vídeo 3 de 3"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape4
    "mixtape4": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 4"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 4"},
        {"file_id": "FILE_ID_3", "caption": "🎬 Vídeo 3 de 4"},
        {"file_id": "FILE_ID_4", "caption": "🎬 Vídeo 4 de 4"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape5
    "mixtape5": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 5"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 5"},
        {"file_id": "FILE_ID_3", "caption": "🎬 Vídeo 3 de 5"},
        {"file_id": "FILE_ID_4", "caption": "🎬 Vídeo 4 de 5"},
        {"file_id": "FILE_ID_5", "caption": "🎬 Vídeo 5 de 5"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape6
    "mixtape6": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 6"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 6"},
        {"file_id": "FILE_ID_3", "caption": "🎬 Vídeo 3 de 6"},
        {"file_id": "FILE_ID_4", "caption": "🎬 Vídeo 4 de 6"},
        {"file_id": "FILE_ID_5", "caption": "🎬 Vídeo 5 de 6"},
        {"file_id": "FILE_ID_6", "caption": "🎬 Vídeo 6 de 6"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape7
    "mixtape7": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 7"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 7"},
        {"file_id": "FILE_ID_3", "caption": "🎬 Vídeo 3 de 7"},
        {"file_id": "FILE_ID_4", "caption": "🎬 Vídeo 4 de 7"},
        {"file_id": "FILE_ID_5", "caption": "🎬 Vídeo 5 de 7"},
        {"file_id": "FILE_ID_6", "caption": "🎬 Vídeo 6 de 7"},
        {"file_id": "FILE_ID_7", "caption": "🎬 Vídeo 7 de 7"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape8
    "mixtape8": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 8"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 8"},
        {"file_id": "FILE_ID_3", "caption": "🎬 Vídeo 3 de 8"},
        {"file_id": "FILE_ID_4", "caption": "🎬 Vídeo 4 de 8"},
        {"file_id": "FILE_ID_5", "caption": "🎬 Vídeo 5 de 8"},
        {"file_id": "FILE_ID_6", "caption": "🎬 Vídeo 6 de 8"},
        {"file_id": "FILE_ID_7", "caption": "🎬 Vídeo 7 de 8"},
        {"file_id": "FILE_ID_8", "caption": "🎬 Vídeo 8 de 8"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape9
    "mixtape9": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 9"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 9"},
        {"file_id": "FILE_ID_3", "caption": "🎬 Vídeo 3 de 9"},
        {"file_id": "FILE_ID_4", "caption": "🎬 Vídeo 4 de 9"},
        {"file_id": "FILE_ID_5", "caption": "🎬 Vídeo 5 de 9"},
        {"file_id": "FILE_ID_6", "caption": "🎬 Vídeo 6 de 9"},
        {"file_id": "FILE_ID_7", "caption": "🎬 Vídeo 7 de 9"},
        {"file_id": "FILE_ID_8", "caption": "🎬 Vídeo 8 de 9"},
        {"file_id": "FILE_ID_9", "caption": "🎬 Vídeo 9 de 9"}
    ],

    # Para enlace: https://t.me/TuBotUsername?start=mixtape10
    "mixtape10": [
        {"file_id": "FILE_ID_1", "caption": "🎬 Vídeo 1 de 10"},
        {"file_id": "FILE_ID_2", "caption": "🎬 Vídeo 2 de 10"},
        {"file_id": "FILE_ID_3", "caption": "🎬 Vídeo 3 de 10"},
        {"file_id": "FILE_ID_4", "caption": "🎬 Vídeo 4 de 10"},
        {"file_id": "FILE_ID_5", "caption": "🎬 Vídeo 5 de 10"},
        {"file_id": "FILE_ID_6", "caption": "🎬 Vídeo 6 de 10"},
        {"file_id": "FILE_ID_7", "caption": "🎬 Vídeo 7 de 10"},
        {"file_id": "FILE_ID_8", "caption": "🎬 Vídeo 8 de 10"},
        {"file_id": "FILE_ID_9", "caption": "🎬 Vídeo 9 de 10"},
        {"file_id": "FILE_ID_10", "caption": "🎬 Vídeo 10 de 10"}
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if args:
        clave = args[0]  # Ejemplo: mixtape5

        if clave in MIXTAPES:
            lista_videos = MIXTAPES[clave]
            total = len(lista_videos)
            
            await update.message.reply_text(f"¡Hola! Te estoy enviando {total} vídeo(s)...")

            # Entregar los vídeos en orden
            for video in lista_videos:
                await context.bot.send_video(
                    chat_id=update.effective_chat.id,
                    video=video["file_id"],
                    caption=video["caption"]
                )
        else:
            await update.message.reply_text("⚠️ El enlace utilizado no es válido o ha caducado.")
    else:
        await update.message.reply_text(
            "👋 ¡Hola! Para recibir el contenido, entra a través de los enlaces de nuestro canal."
        )

if __name__ == '__main__':
    print("Bot con estructura Mixtapes (1-10) en marcha...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()