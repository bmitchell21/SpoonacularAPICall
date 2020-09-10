#!/usr/bin/python

import sys 
import config
import requests
import json

Key = config.api_key
ingredientURLParams = {
    'ingredients': str(sys.argv),
    'number': 1,
    'ranking': 1,
    'apiKey': Key
}

rStepsURLParams = {
    'apiKey': Key,
    'includeNutrition' : False
}

recipe = requests.get("https://api.spoonacular.com/recipes/findByIngredients", params=ingredientURLParams)
recipeJSON = recipe.json()
recipeID = (recipeJSON[0]['id'])
missedIngredients = (recipeJSON[0]['missedIngredients']['original'])
stringID = str(recipeID)

instructions = requests.get("https://api.spoonacular.com/recipes/" + stringID + "/information", params=rStepsURLParams)
instructionsJSON = instructions.json()
followalong = (instructionsJSON['sourceUrl'])

print(missedIngredients)
print(followalong) 
