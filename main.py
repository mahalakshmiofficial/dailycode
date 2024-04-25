# import constants as key 
from constants import API_KEY
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
    user_message = update.message.text.lower()
    if user_message in ("hello", "hi", "good morning", "hey"):
        response =  "hey!WELCOME to Madurai startups.Are you looking for office / co working / events / free lancers/ jobs / showcase"
    elif user_message in ("yes, i am looking for office", "office"):
        response = "we have offices from 4 people and above.?How many people do you have on a team"
    elif user_message in ("4", "5", "6"):
        response = "okay will update you the details.Do you want to book(yes/no)"
    elif user_message in ("yes", "yes,i want to book"):
        response =  "okay,please do specify your mail id. we will update you via mail soon.have a nice day"
    elif user_message in "no":
        response =  "okay,Thankyou.let us know if you need any help."
    elif user_message in "co working":
        response = "We offer a Floating work place from 400 rs per day,Do you want to book(yes/no)?"
    elif user_message in "events":
        response = "here are our events.please do check https://maduraistartups.in/events/. Do you want to book or" , "organise any events?"
    elif user_message in ("freeLancers","free lancer","free lancer"):
        response =  "what Domain you are looking for? and  also specify your mail id to  get notified "
    elif user_message in ("job","jobs"):
        response =  "do check here.https://maduraistartups.in/job-openings/,and specify your mail id"
    elif user_message in ("showcases","showcase","product Showcase"):
        response = "do check here. https://maduraistartups.in/showcase"
    elif user_message in "Thankyou":
        response = "we are here to assist you anytime.Thanks"  
    else:
        response = "Sorry I Don't Know"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
if __name__ == "__main__":
    application = ApplicationBuilder().token(API_KEY).build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.run_polling()
