import requests

API_KEY = "86e2f970f3d307388da5c09be5b694fb"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        rainfall = data.get("rain", {}).get("1h", 0)

        return temperature, humidity, rainfall

    else:
        return None


# Test
result = get_weather("Chittagong")
print(result)