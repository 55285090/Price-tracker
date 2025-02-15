import json
import requests
from bs4 import BeautifulSoup

DATA_FILE = "price_data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def fetch_price(url, selector):
    """Scrape product price from URL using CSS selector."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    price_element = soup.select_one(selector)
    return price_element.text.strip() if price_element else "N/A"

def check_prices():
    """Check prices and update the JSON file."""
    data = load_data()
    for product, details in data.items():
        new_price = fetch_price(details["url"], details["selector"])
        if new_price and new_price != details["last_price"]:
            print(f"Price changed for {product}: {details['last_price']} → {new_price}")
            data[product]["last_price"] = new_price
    save_data(data)

if __name__ == "__main__":
    check_prices()  # ✅ Runs once and exits
