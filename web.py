#web.py

from flask import Flask, render_template, request
from weather import get_weather
import os

app = Flask(__name__)

@app.route("/")
def index():
    name = request.values.get('name') #use the get method
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weather')
def weather():
    address = request.values.get('address')
    weather = None
    if address:
        weather = get_weather(address)
    return render_template('weather.html', address=address, weather=weather)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
