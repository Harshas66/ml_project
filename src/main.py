from src.data_loader import load_data
from src.feature_engineering import prepare_inventory, prepare_recipes
from src.recipe_feasibility import check_feasibility
from src.recommender import recommend_recipes

def main():
    # Load datasets
    inventory, recipes = load_data()

    # Prepare features
    inventory = prepare_inventory(inventory)
    recipes = prepare_recipes(recipes)

    # Check recipe feasibility
    feasible, partial, not_possible = check_feasibility(inventory, recipes)

    print("Recipes you can cook now:", feasible[:5])
    print("Recipes partially possible:", partial[:5])
    print("Recipes not possible:", not_possible[:5])

    # Recommend recipes
    recommendations = recommend_recipes(inventory, recipes)
    print("\n📌 Recommended Recipes:", recommendations[:5])

if __name__ == "__main__":
    main()
