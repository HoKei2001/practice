import os
import httpx

from dotenv import load_dotenv

class WeatherService:
    def __init__(self,api_key:str) -> None:
        self.api_key = api_key

    def get_temperature(self, city:str) -> float:
        response = httpx.get(
            "https://api.weatherapi.com/v1/current.json",
            params= {"key":self.api_key,"q":city},
        )
        response.raise_for_status()
        data = response.json()
        return data["current"]["temp_c"]

def main():
    load_dotenv()  # Load environment variables from .env file
    service = WeatherService(api_key=os.getenv("WEATHER_API_KEY"))
    temp = service.get_temperature("Singapore")
    print(f"The temperature in Singapore is {temp}°C")

if __name__ == "__main__":
    main()