# CS LAB 01 presenting the API aatempts

import requests

def listIngred():

    baseUrl = "https://wizard-world-api.herokuapp.com/Ingredients"
    #endpoint = baseUrl + language
    resp = requests.get(baseUrl)
    data = resp.json()
    
    #print(data)
    #print(data[0])
    #print(data[0]["name"])

    allIngredients = []

    for i in range(len(data)):
        allIngredients.append(data[i]["name"])

    allIngredients = sorted(allIngredients)
    #return (allIngredients)


#print(listIngred())


def whatElixirs(chosenIngred):

    baseUrl = "https://wizard-world-api.herokuapp.com/Elixirs"
    #endpoint = baseUrl + language
    resp = requests.get(baseUrl)
    data = resp.json()

    # for every elixir in elixirs
    # if ingred = chosen ingred then
    # append possible spells list

    possibleElixirs = []

    """
    print(data[0])
    print(data[0]["effect"])
    print(data[0]["ingredients"])
    for item in (data[0]["ingredients"]):
        print (item)
        print (item["name"])
        ingredients.append(item["name"])
    print (ingredients)
    """

    """
    #print (data[5]["characteristics"])
    if (data[0]["characteristics"]) != "":
        print (data[0]["characteristics"])
    else:
        print ("None listed")
    """
    
    characteristics = data[5]["characteristics"]
    if not characteristics:
        print("None listed")
    else:
        print(characteristics)

    for i in range(len(data)):
        name = (data[i]["name"])
        effect = (data[i]["effect"])
        ingredients = []
        for item in (data[i]["ingredients"]):
            ingredients.append(item["name"])
        if chosenIngred in ingredients or (chosenIngred + "s") in ingredients:
            possibleElixirs.append( (name, effect, ingredients))

    return (possibleElixirs)


#print(whatElixirs("Newt spleen"))

def sortClasses(classByType):
    
    baseUrl = "https://wizard-world-api.herokuapp.com/Spells"
    #endpoint = baseUrl + language
    resp = requests.get(baseUrl)
    data = resp.json()

    #print(data[0])
    #print(data[0]["type"])

    classSpells = []

    for i in range(len(data)):
        spellType = data[i]["type"]
        spellName = data[i]["name"]
        if spellType == classByType:
            classSpells.append(spellName)

    return(classSpells)
                     
#print(sortClasses("Transfiguration"))

def sortClasses2(whosList):
    
    baseUrl = "https://wizard-world-api.herokuapp.com/Spells"
    #endpoint = baseUrl + language
    resp = requests.get(baseUrl)
    data = resp.json()

    #print(data[0])
    #print(data[0]["type"])

    classSpells = []
    McList =[]
    FlitList =[]
    MoodList =[]

    for i in range(len(data)):
        spellType = data[i]["type"]
        spellName = data[i]["name"]
        if spellType == "Transfiguration":
            McList.append(spellName)
        elif spellType == "Charm":
            FlitList.append(spellName)
        else:
            MoodList.append(spellName)
        
    if whosList == "McList":
        return McList
    elif whosList == "FlitList":
        return FlitList
    elif whosList == "MoodList":
        return MoodList
    else:
        return []
                     
print(sortClasses2("McList"))


