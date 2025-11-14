# this will be Phase 2: Web API Analysis

import requests
import streamlit as st
import pandas as pd

tab1, tab2, tab3, tab4 = st.tabs(["Snape's Class", "Flitwick's Class", "McGonigle's Class", "Moody's Class"])

# EXLIXIRS FUNC

with tab1:
    st.header("Welcome to Potions")
    def DifficultyGraphElixir():
        baseurl = "https://wizard-world-api.herokuapp.com/Elixirs"
        resp = requests.get(baseurl)
        data = resp.json()
        difficultyDict = {}
        for i in range(len(data)):
            name = (data[i]["name"])
            difficulty = (data[i]["difficulty"])
            difficultyDict[name] = difficulty
            #print(difficulty)
            #print(type(name))
            #return name
        #return difficultyDict
        df = pd.DataFrame({
            "Elixirs": list(difficultyDict.keys()),
            "Difficulty": list(difficultyDict.values()
                               )})
        all_difficulties = sorted(df["Difficulty"].unique())

        if "selected_difficulties" not in st.session_state:
            st.session_state.selected_difficulties = all_difficulties

        selected = st.multiselect(
            "Filter by Difficulty:",
            options=all_difficulties,
            default=st.session_state.selected_difficulties,
            key="selected_difficulties"
        )

        filtered_df = df[df["Difficulty"].isin(st.session_state.selected_difficulties)]
        difficulty_counts = filtered_df["Difficulty"].value_counts().reset_index()
        difficulty_counts.columns = ["Difficulty", "Count"]

        st.bar_chart(data=difficulty_counts, x="Difficulty", y="Count")

    print(DifficultyGraphElixir())
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
        return (allIngredients)

    st.write("Snapes class! Lets learn about potions and elixirs!")
    st.image("Images/SnapesClass.jpg", width=400)

    chosenIngred = st.selectbox(
        "Pick an ingredient you found in snapes cabinet to make a potion",
        (listIngred()),
        index=None,
        placeholder="Choose carefully...",
    )
             
    def whatElixirs(chosenIngred):

        baseUrl = "https://wizard-world-api.herokuapp.com/Elixirs"
        #endpoint = baseUrl + language
        resp = requests.get(baseUrl)
        data = resp.json()

        possibleElixirs = []

        for i in range(len(data)):
            name = (data[i]["name"])
            effect = (data[i]["effect"])
            characteristics = data[i]["characteristics"]
            sideEffects = data[i]["sideEffects"]
            ingredients = []
            for item in (data[i]["ingredients"]):
                ingredients.append(item["name"])
            if chosenIngred in ingredients or (chosenIngred + "s") in ingredients:
                possibleElixirs.append((name, effect, characteristics, sideEffects, ingredients))

        return (possibleElixirs)

    if chosenIngred != None:
        st.write("These are all the elixirs you can make with that to impress Snape!")
        for name, effect, characteristics, sideEffects, ingredients in whatElixirs(chosenIngred):
            expander = st.expander(name)
            expander.write(f"**Effect:** {effect}")
            if characteristics:
                expander.write(f"**Characteristics:** {characteristics}")
            if sideEffects:
                expander.write(f"**Side Effects:** {sideEffects}")
            expander.write("**All Ingredients:**")
            for ingred in ingredients:
                expander.write(f"- {ingred}")
            
# SPELLS FUNCS

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
        incantation = data[i]["incantation"]
        effect = data[i]["effect"]
        light = data[i]["light"]
        creator = data[i]["creator"]
        if spellType == "Transfiguration":
            McList.append((spellName, incantation, effect, light, creator))
        elif spellType == "Charm":
            FlitList.append((spellName, incantation, effect, light, creator))
        else:
            MoodList.append((spellName, incantation, effect, light, creator))
        
    if whosList == "McList":
        return McList
    elif whosList == "FlitList":
        return FlitList
    elif whosList == "MoodList":
        return MoodList
    else:
        return []
        

    
with tab2:
    allCharms = sortClasses2("FlitList")
    allCharmsNames = []
    for spellName, incantation, effect, light, creator in allCharms:
        allCharmsNames.append(spellName)

    st.header("Welcome to Charms")
    st.write("This is Flitwicks class! Lets learn about charms!")
    st.image("Images/FlitwicksClass.jpg", width=400)
    def DifficultyGraphSpells():
        baseurl = "https://wizard-world-api.herokuapp.com/Spells"
        resp = requests.get(baseurl)
        data = resp.json()
        spellDict = {}
        for i in range(len(data)):
            names = (data[i]["name"])
            spellType = (data[i]["type"])
            spellDict[names] = spellType
        #return spellDict
        df = pd.DataFrame({
            "Spells": list(spellDict.keys()),
            "Type": list(spellDict.values()
                               )})
        all_types = sorted(df["Type"].unique())

        if "all_types" not in st.session_state:
            st.session_state.all_types = all_types

        selected = st.multiselect(
            "Filter by type:",
            options=all_types,
            default=st.session_state.all_types,
            key="all_types"
        )

        filtered_df = df[df["Type"].isin(st.session_state.all_types)]
        difficulty_counts = filtered_df["Type"].value_counts().reset_index()
        difficulty_counts.columns = ["Type", "Count"]

        st.bar_chart(data=difficulty_counts, x="Type", y="Count")
    print(DifficultyGraphSpells())

    chosenCharm = st.selectbox(
        "Pick a charm to learn",
        (allCharmsNames),
        index=None,
        placeholder="Choose carefully...",
    )

    if chosenCharm != None:
        st.write("Cast the charm to impress Flitwick!")
        for spellName, incantation, effect, light, creator in allCharms:
            if spellName == chosenCharm:
                st.subheader(spellName)
                st.write(f"**Incantation:** {incantation}")
                if effect:
                    st.write(f"**Effect:** {effect}")
                if light:
                    st.write(f"**Light:** {light}")
                if creator:
                    st.write(f"**Creator:** {creator}")
    
    
with tab3:
    allTrans = sortClasses2("McList")
    allTransNames = []
    for spellName, incantation, effect, light, creator in allTrans:
        allTransNames.append(spellName)

    st.write("This is McGonagalls class! Lets learn about transfiguration!")
    st.image("Images/McGonagallsClass.jpg", width=400)

    chosenTrans = st.selectbox(
        "Pick a transfiguration spell to learn",
        (allTransNames),
        index=None,
        placeholder="Choose carefully...",
    )

    if chosenTrans != None:
        st.write("Cast the spell to impress McGonagall!")
        for spellName, incantation, effect, light, creator in allTrans:
            if spellName == chosenTrans:
                st.subheader(spellName)
                st.write(f"**Incantation:** {incantation}")
                if effect:
                    st.write(f"**Effect:** {effect}")
                if light:
                    st.write(f"**Light:** {light}")
                if creator:
                    st.write(f"**Creator:** {creator}")

with tab4:
    allElse = sortClasses2("MoodList")
    allElseNames = []
    for spellName, incantation, effect, light, creator in allElse:
        allElseNames.append(spellName)

    
    st.write("Moodys class! Lets learn about defense against the dark arts!")
    st.image("Images/MoodysClass.png", width=400)

    chosenElse = st.selectbox(
        "Pick a transfiguration spell to learn",
        (allElseNames),
        index=None,
        placeholder="Choose carefully...",
    )

    if chosenElse != None:
        st.write("Cast the spell to impress Moody!")
        for spellName, incantation, effect, light, creator in allElse:
            if spellName == chosenElse:
                st.subheader(spellName)
                st.write(f"**Incantation:** {incantation}")
                if effect:
                    st.write(f"**Effect:** {effect}")
                if light:
                    st.write(f"**Light:** {light}")
                if creator:
                    st.write(f"**Creator:** {creator}")


                    
