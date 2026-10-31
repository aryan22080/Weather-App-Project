import requests
api = "97bf8f80232e953a88b9b9e1d67aaf96"
weather = input("Enter the city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={weather}&appid={api}&units=metric"
if not weather:
    print("Please enter a city name.")
else:
    response = requests.get(url)
    print(response.status_code)
    weather_data = response.json()
    print(weather_data)
