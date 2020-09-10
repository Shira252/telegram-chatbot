import logging
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters, RegexHandler
import requests
import re
import random
import telegram
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)
 
line = "Welcome to the HappyChatter, I'm Shira, glad to see you and serve you.\nNow I will take a few time to introduce my function to you.\n(1) There are 4 buttons, for the first button, you can give me some special needs like you hate which food, your calories limits in one day, or your habit for eating. \n(2) For the second button, you can find the video about cook, and learn how to cook. \n(3) For the third button, give me a name for a receipt, I can give you its nutrients contain calories,protein \n(4) For the forth button, you can ask me some questions or just chat with me. \nHope that you have a good time "
def start(bot, update):
    kb = [[telegram.KeyboardButton('Generate the meal plan')],
          [telegram.KeyboardButton('Find the cook video')],
         [telegram.KeyboardButton("Analyze the nutrients")],
         [telegram.KeyboardButton("Happy chat")]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb)
    bot.send_message(chat_id=update.message.chat_id,text=line,reply_markup=kb_markup)


aList = []
def hide(bot,update):
    if "Generate the meal plan" in update.message.text:
        aList.append("Generate the meal plan")
        bot. send_message(chat_id=update.message.chat_id, text = "Befor give you my advice, I would like to ask do you have any special needs that I should pay attention on",reply_markup = telegram.ReplyKeyboardRemove())
    if "Find the cook video" in update.message.text:
        aList.append("Find the cook video")
        bot. send_message(chat_id=update.message.chat_id, text = "There are a lot of videos, I'm confused which dishes you would like to find the relative video",reply_markup = telegram.ReplyKeyboardRemove())
    if "Analyze the nutrients" in update.message.text:
        aList.append("Analyze the nutrients")
        bot. send_message(chat_id=update.message.chat_id, text = "Give me a specific name for the receipe that you want to have the specific information, I will analyze the nutrients for you",reply_markup = telegram.ReplyKeyboardRemove())
    if "Happy chat" in update. message.text:
        aList.append("Happy chat")
        bot. send_message(chat_id=update.message.chat_id, text = "Happy to see you!!! Do you have any question or any thoughts that want to chat with me",reply_markup = telegram.ReplyKeyboardRemove())
