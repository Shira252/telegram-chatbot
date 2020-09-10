def search(message):
    aString = ""
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/detect"
    payload = "text=" + message
    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "c4b855b7dfmshbc032041d307865p10b87ejsn8e37aa9ca505",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers).json()
    for i in response["annotations"]:
        aString = aString + i["annotation"] +", "
    return aString

def getDiet(message):
    aString = ""
    if "vegan" in message:
        aString = "vegan"
    elif "vegetarian" in message:
        aString = "vegetarian"
    elif "paleo" in message:
        aString = "paleo"
    return aString

def generatemealplan(message):
    if getNum(message) == "":
        num = "2000"
    else:
        num = getNum(message)
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"
    querystring = {"timeFrame":"day","targetCalories":num,"diet":getDiet(message),"exclude":search(message)}
    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "c4b855b7dfmshbc032041d307865p10b87ejsn8e37aa9ca505"
    }
    response = requests.get(url, headers=headers, params=querystring).json()
    return response

def respond1(message):
        response=generatemealplan(message)
        return response["meals"] [random.randint(0,2)]["sourceUrl"]

def mode1(bot,update):
    if "change" in update.message.text:
        bot.send_message(chat_id=update.message.chat_id, text="This is another one, if you have any other special needs or you want to change again,you can tell me ")
        bot.send_message(chat_id=update.message.chat_id, text=respond1(update.message.text))
    elif "don't" in update.message.text or "calories" in update.message.text or "vegan" in update.message.text or "paleo" in update.message.text:
        bot.send_message(chat_id=update.message.chat_id, text="Below is the advice, hope that you can love it")
        bot.send_message(chat_id=update.message.chat_id, text=respond1(update.message.text))
    
