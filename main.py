import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Logging ayarı
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Canlı Skorlar", callback_data="live")],
        [InlineKeyboardButton("Lig Seç", callback_data="leagues")],
        [InlineKeyboardButton("Transfer Haberleri", callback_data="transfers")],
        [InlineKeyboardButton("Favori Takımlarım", callback_data="favorites")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "Merhaba!\n\n"
        "Basketbol Gündem Botuna hoş geldiniz.\n\n"
        "Bu bot ile:\n"
        "• NBA, EuroLeague ve Türkiye Basketbol Süper Ligi puan durumlarını\n"
        "• Fikstür ve yaklaşan maçları\n"
        "• Canlı skorları\n"
        "• Transfer haberlerini\n\n"
        "kolayca takip edebilirsiniz.\n\n"
        "Bot yalnızca gerçek ve güncel veriler sunar. Tahmin, oran veya bahis içeriği bulunmamaktadır.\n\n"
        "Başlamak için aşağıdaki menüyü kullanabilirsiniz."
    )

    await update.message.reply_text(text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "live":
        await query.edit_message_text("Canlı skorlar yakında aktif olacak.")
    elif query.data == "leagues":
        await query.edit_message_text("Lig seçimi yakında aktif olacak.")
    elif query.data == "transfers":
        await query.edit_message_text("Transfer haberleri yakında aktif olacak.")
    elif query.data == "favorites":
        await query.edit_message_text("Favori takım özelliği yakında aktif olacak.")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN bulunamadı! Render Environment kısmını kontrol et.")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Render için en stabil yöntem
    application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)

if __name__ == "__main__":
    main()
