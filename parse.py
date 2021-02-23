import json
f = open("url.txt", "r")
s = f.read()

def findIngredient():
    start = s.find('"recipeIngredient": [') 
    end = start
    while s[end] != ']':
        end += 1
    return s[start:end+1]

print(findIngredient())
print("\n\n")



def findDirection():
    start = s.find('"recipeInstructions": [') 
    end = start
    while s[end] != ']':
        end += 1
    jsonObj = json.loads("{" + s[start:end+1] + "}")
    return jsonObj

print(json.dumps(findDirection(), indent=4, sort_keys=True))
print("\n\n")

