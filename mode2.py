def searchvideo(message):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/videos/search"

    querystring = {"query":query(message),"excludeingredients":"mustard","includeingredients":search(message),"minLength":"0","maxLength":"999","offset":"0","number":"10"}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "c4b855b7dfmshbc032041d307865p10b87ejsn8e37aa9ca505"
        }

    response = requests.get(url, headers=headers, params=querystring).json()
    num = random.randint(0,5)
    aString = "https://www.youtube.com/watch?v=" + response["videos"][num]["youTubeId"]
    return aString

def mode2(bot,update):
    if search(update.message.text)!="":
        bot.send_message(chat_id=update.message.chat_id, text="This is the video, hope that it can help you")
        bot.send_message(chat_id=update.message.chat_id, text=searchvideo(update.message.text),supports_streaming=True)
