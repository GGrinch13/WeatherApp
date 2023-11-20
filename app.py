import requests
from flask import Flask, render_template, request


app = Flask(__name__)
api_key = "138eb12bb53a4dc3980163106232204"

def get_weather(city):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url).json()
        temp_c = response["current"]["temp_c"]
        feelslike_c = response["current"]["feelslike_c"]
        temp_f = response["current"]["temp_f"]
        feelslike_f = response["current"]["feelslike_f"]
        is_day = response["current"]["is_day"]
        wind_mph = response["current"]["wind_mph"]
        wind_kph = response["current"]["wind_kph"]
        humidity = response["current"]["humidity"]
        local_time = response["location"]["localtime"]
        text = response["current"]["condition"]["text"]
        icon = response["current"]["condition"]["icon"]
        return {'temp_c': temp_c, 'feelslike_c': feelslike_c,
            'temp_f': temp_f, 'feelslike_f': feelslike_f,
            'is_day': is_day, 'wind_mph': wind_mph,
            'wind_kph': wind_kph, 'humidity': humidity,
            'local_time': local_time, 'text': text, 'icon': icon}
    except KeyError:
        return {'error': 'Please enter a valid city name.'}


@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index_page():
    if request.method == "POST":
        city = request.form.get("city")
        result = get_weather(city)
        return render_template("index.html", **result)
    return render_template("index.html"), 200


@app.route("/about.html")
def about_page():
    return render_template("about.html"), 200


# Uncomment this if developing
# with app.app_context():
#    app.run()