def find(message):
    aString = ""

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition"

    querystring = {"title":message}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "c4b855b7dfmshbc032041d307865p10b87ejsn8e37aa9ca505"
        }

    response = requests.get(url, headers=headers, params=querystring).json()
    aString = aString +"calories: "+str(response["calories"]["value"]) +" " + str(response["calories"]["unit"]) + ", fat: " + str(response["fat"]["value"]) + " " +str(response["fat"]["unit"])+", protein: "+str(response["protein"]["value"])+" "+str(response["protein"]["unit"])+", carbs: "+str(response["carbs"]["value"]) +" "+str(response["carbs"]["unit"])
    return aString

def mode3(bot,update):
    if "name" in update.message.text: 
        bot.send_message(chat_id=update.message.chat_id, text=find(update.message.text[5:]))
