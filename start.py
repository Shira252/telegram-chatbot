import logging
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters, RegexHandler
import requests
import re
import random
import telegram
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)
 
