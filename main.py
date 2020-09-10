import random
def respond(bot,update):
    # Call the match_intent function
    
    intent = match_intent(update.message.text)
    # Fall back to the default response
    key =""
    if intent in responses:
        key = intent
    name = find_name(update.message.text)
    hide(bot,update)
    if "change" in update.message.text and "mode" in update.message.text:
        start(bot,update)
    elif aList[-1] == "Generate the meal plan":
        mode1(bot,update)
    elif aList[-1] == "Find the cook video":
        mode2(bot,update)
    elif aList[-1] == "Analyze the nutrients":
        mode3(bot,update)
    elif aList[-1] == "Happy chat":
        mode4(bot,update)
    if key == "greet" or key == 'thankyou' or key =='goodbye':
        bot.send_message(chat_id=update.message.chat_id, text=responses[key])


