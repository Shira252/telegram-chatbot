keywords = {
            'greet': ['hello', 'hi', 'hey','name','call','Hello','Hi'], 
            'thankyou': ['thank', 'thx','Thank'], 
            'goodbye': ['bye', 'farewell','Bye']
           }
# Define a dictionary of patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    
    # Create regular expressions and compile them into pattern objects
    patterns[intent] =re.compile('|'.join(keys))
responses = {
             'thankyou': 'you are very welcome',  
             'goodbye': 'goodbye for now',
             
            }

# Define a function to find the intent of a message
def match_intent(message):
    message.lower()
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        
        if re.search(pattern,message):
            matched_intent = intent
        
    return matched_intent

def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword= re.compile("name|call")
    # Create a pattern for finding capitalized words
    name_pattern = re.compile("[A-Z]{1}[a-z]*")
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
    return name
