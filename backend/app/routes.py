from flask import Blueprint, jsonify

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipes", methods=["GET"])
def get_recipes():
    # Example data
    recipes = [
        {"id": 1, "name": "Spaghetti Bolognese", "ingredients": ["spaghetti", "tomato sauce", "ground beef"]},
        {"id": 2, "name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "coconut milk"]}
    ]
    return jsonify(recipes)