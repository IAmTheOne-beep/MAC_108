class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

class WeatherAPIClient:
    def get_temperature(self, city):
        
        #1. Attach city parameter
        url = f"{self.base_url}/weater"
        params = {"q": city, "appid": self.api_key}

        #2. Execute request.get() call
        response = requests.get(url, params=params)

        #3. Verify 200 OK status code
        if response.status_code == 200:
            return response.json()

weather_bot = WeatherAPI()

temp = weather_bot.get_temperature("New York")