from flask import Flask, render_template
import json

app = Flask(__name__)

def load_prices():
    """Load product prices from JSON file."""
    try:
        with open("price_data.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

@app.route("/")
def home():
    prices = load_prices()  # Load tracked prices
    return render_template("index.html", prices=prices)

if __name__ == "__main__":
    app.run(debug=True)
