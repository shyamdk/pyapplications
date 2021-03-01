import json

data = json.load(open("files/1data.json"))

def get_meaning(A):
    return data[A] 

word = input("Enter a word: ")

print(get_meaning(word))