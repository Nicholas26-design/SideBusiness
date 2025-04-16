from flask import Flask
from app.routes import recipe_routes

app = Flask(__name__)

# Register API routes
app.register_blueprint(recipe_routes)

@app.route("/")
def index():
    return {"message": "Welcome to FoodApp API!"}

if __name__ == "__main__":
    app.run(debug=True)