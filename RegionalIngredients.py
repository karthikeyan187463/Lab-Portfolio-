# Define Zelda regions with ingredients and assigned values for Link
zelda_recipe_guide = {
    "Hebra Mountains": {"Icy Radish": 9, "Frost Carrot": 6},
    "Gerudo Desert": {"Desert Cactus": 7, "Spicy Pepper": 5},
    # Region with missing ingredients
    "Akkala Highlands": {}  # Bug: No ingredients listed here
}

# Expected ingredients for each region in BOTW
expected_ingredients_botw = {
    "Hebra Mountains": ["Icy Radish", "Frost Carrot"],
    "Gerudo Desert": ["Desert Cactus", "Spicy Pepper"],
    "Akkala Highlands": ["Voltfruit", "Armoranth"]  # Missing ingredients expected here
}

# Correct values for each ingredient in BOTW
correct_ingredient_values = {
    "Icy Radish": 9, "Frost Carrot": 6, "Desert Cactus": 7, "Spicy Pepper": 5,
    "Voltfruit": 8, "Armoranth": 4
}

# Function to validate ingredients and update values as needed
def validate_botw_ingredients(recipe_guide, expected_ingredients, correct_values):
    for region, ingredients in expected_ingredients.items():
        print(f"\nValidating ingredients for {region}...")

        # Check for missing ingredients
        missing_ingredients = [item for item in ingredients if item not in recipe_guide[region]]
        if missing_ingredients:
            print(f"  Missing ingredients: {missing_ingredients}")
            # Add missing ingredients with correct values
            for item in missing_ingredients:
                recipe_guide[region][item] = correct_values[item]
            print(f"  Added missing ingredients with correct values.")
        else:
            print("  All ingredients are present.")

        # Check for value inconsistencies and correct them
        for ingredient, value in recipe_guide[region].items():
            if value != correct_values[ingredient]:
                print(f"  Incorrect value for {ingredient}: {value} (Expected: {correct_values[ingredient]})")
                recipe_guide[region][ingredient] = correct_values[ingredient]
                print(f"  Updated {ingredient} to correct value.")
            else:
                print(f"  {ingredient} value is correct.")

# Run validation on Zelda recipe guide
validate_botw_ingredients(zelda_recipe_guide, expected_ingredients_botw, correct_ingredient_values)

# Display the updated Zelda recipe guide
print("\nUpdated Zelda Recipe Guide:", zelda_recipe_guide)
