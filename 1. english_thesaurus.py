import json
import difflib

data = json.load(open("files/1data.json"))

def get_meaning(w):
    if w in data:
        return data[w] 
    else:
        return "The word does not exist, please check again."
word = input("Enter a word: ")

print(get_meaning(word.lower()))