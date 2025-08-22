import pandas as pd

def check_feasibility(inventory_df: pd.DataFrame, recipes_df: pd.DataFrame):
    """
    Classify recipes into feasible, partial, and not possible
    based on available inventory.
    
    Args:
        inventory_df (pd.DataFrame): Grocery inventory dataset
        recipes_df (pd.DataFrame): Recipe dataset
    
    Returns:
        tuple: (feasible, partial, not_possible)
    """
    # Ensure ingredients column exists
    if "ingredients" not in recipes_df.columns:
        raise ValueError("Recipes dataset must have an 'ingredients' column")

    # Clean inventory product names (lowercase for matching)
    available_items = set(inventory_df["Product_Name"].str.lower().str.strip())

    feasible = []
    partial = []
    not_possible = []

    # Loop over recipes
    for idx, row in recipes_df.iterrows():
        recipe_name = row["name"]
        recipe_ingredients = str(row["ingredients"]).lower().split(",")  # assuming comma-separated
        recipe_ingredients = [ing.strip() for ing in recipe_ingredients]

        # Find available ingredients
        available = [ing for ing in recipe_ingredients if any(item in ing for item in available_items)]

        if len(available) == len(recipe_ingredients):
            feasible.append(recipe_name)
        elif len(available) > 0:
            partial.append(recipe_name)
        else:
            not_possible.append(recipe_name)

    return feasible, partial, not_possible
