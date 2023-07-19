from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        postal_code = request.form['postal_code']
        weather = get_weather(postal_code)
        return render_template('index.html', weather=weather)
    else:
        return render_template('index.html')

def get_weather(postal_code):
    api_key = ""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = base_url + "?appid=" + api_key + "&zip=" + postal_code
    response = requests.get(complete_url)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)
