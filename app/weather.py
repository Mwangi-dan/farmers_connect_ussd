import requests


def fetch_weather_forecast():
    api_key = 'dd87517a20c9aae27dec177027893a43'
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    city_name = "Freetown,SL"  # Sierra Leone's capital, Freetown
    units = "metric"  # or "imperial" for Fahrenheit
    days  = 1

    # Construct the API URL
    url = f"{base_url}?q={city_name}&units={units}&cnt={days}&appid={api_key}"

    # Send the HTTP GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Convert the response to JSON format
        return data
    else:
        print("Error fetching weather data.")
        return None


