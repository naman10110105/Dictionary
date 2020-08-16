import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def dictionary(word):

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        suggestion = input("Did you mean " + get_close_matches(word,
                                                               data.keys(), cutoff=0.8)[0] + "? (Press Y or N): ").lower()
        if suggestion == 'y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        else:
            return "The word does not exist."
    else:
        return "Please enter a valid word."


while True:
    word = input("Please enter the word: ").lower()
    result = dictionary(word)
    if type(result) == list:
        for output in result:
            print(output)
    else:
        print(result)
