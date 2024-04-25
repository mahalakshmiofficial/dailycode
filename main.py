import constants as key
from telegram.ext import*
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Configure logging for informative messages
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Greets the user with a personalized message."""

    user_name = update.effective_chat.first_name if update.effective_chat.first_name else "user"
    await context.bot.send_message(chat_id=update.effective_chat.id,text=f"Hi {user_name}, how can I help you today?")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "youtube" in update.message.text.lower():
        response = f"https://www.youtube.com"
    else:
        response = "Sorry, I don't understand yet. How can I be of service?"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

if __name__ == "__main__":
    application = ApplicationBuilder().token(key).build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.run_polling()