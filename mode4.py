def joke():
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/jokes/random"

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "c4b855b7dfmshbc032041d307865p10b87ejsn8e37aa9ca505"
        }

    response = requests.get(url, headers=headers).json()

    return response["text"]

def fact():
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/trivia/random"

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "c4b855b7dfmshbc032041d307865p10b87ejsn8e37aa9ca505"
        }

    response = requests.get(url, headers=headers).json()

    return response["text"]

def quick(message):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer"

    querystring = {"q":message}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "c4b855b7dfmshbc032041d307865p10b87ejsn8e37aa9ca505"
        }

    response = requests.get(url, headers=headers, params=querystring).json()

    return response["answer"]

def recommend(message):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/recommendation"

    querystring = {"maxPrice":"50","minRating":"0.7","number":"3","wine":search1(message)}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "c4b855b7dfmshbc032041d307865p10b87ejsn8e37aa9ca505"
    }

    response = requests.get(url, headers=headers, params=querystring).json()

    return response["recommendedWines"][0]

def mode4(bot,update):
    if "joke" in update.message.text:
        bot.send_message(chat_id=update.message.chat_id, text="this is a joke that I find for you, hope that you will have a good mood")
        bot.send_message(chat_id=update.message.chat_id, text=joke())
    if "fact" in update.message.text:
        bot.send_message(chat_id=update.message.chat_id, text="There are a lot of amazing things about food, if you want hear, I can tell you more like this")
        bot.send_message(chat_id=update.message.chat_id, text=fact())
    if "?" in update.message.text and search(update.message.text)!="":
        bot.send_message(chat_id=update.message.chat_id, text="Hope that this answer can be helpful for your question")
        bot.send_message(chat_id=update.message.chat_id, text=quick(update.message.text))
    if search2(update.message.text) != "":
        bot.send_message(chat_id=update.message.chat_id, text="This is my recommendation, incuding its title, description and link, hope that you like it")
        bot.send_message(chat_id=update.message.chat_id, text=recommend(update.message.text)["title"])
        bot.send_message(chat_id=update.message.chat_id, text=recommend(update.message.text)["description"])
        bot.send_message(chat_id=update.message.chat_id, text=recommend(update.message.text)["link"])
