"""
Weather API Integration Module
Handles all interactions with OpenWeatherMap API
"""

import requests
from typing import Dict, Optional


class WeatherAPI:
    """Class to handle OpenWeatherMap API requests"""

    BASE_URL = "https://api.openweathermap.org/data/2.5"
    GEO_URL = "https://api.openweathermap.org/geo/1.0"

    def __init__(self, api_key: str):
        """Initialize with API key"""
        self.api_key = api_key

    def get_current_weather(self, city: str = None, lat: float = None, lon: float = None) -> Optional[Dict]:
        """
        Get current weather data for a location

        Args:
            city: City name (Hebrew or English)
            lat: Latitude
            lon: Longitude

        Returns:
            Dictionary with weather data or None if error
        """
        try:
            # If city is provided, get coordinates
            if city:
                coords = self._get_coordinates(city)
                if not coords:
                    return None
                lat, lon = coords['lat'], coords['lon']

            # Make API request
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'en'
            }

            response = requests.get(f"{self.BASE_URL}/weather", params=params)
            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def get_forecast(self, city: str = None, lat: float = None, lon: float = None, days: int = 5) -> Optional[Dict]:
        """
        Get weather forecast

        Args:
            city: City name
            lat: Latitude
            lon: Longitude
            days: Number of days (max 5 for free tier)

        Returns:
            Dictionary with forecast data
        """
        try:
            if city:
                coords = self._get_coordinates(city)
                if not coords:
                    return None
                lat, lon = coords['lat'], coords['lon']

            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'en',
                'cnt': days * 8  # 8 forecasts per day (every 3 hours)
            }

            response = requests.get(f"{self.BASE_URL}/forecast", params=params)
            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            print(f"Error fetching forecast: {e}")
            return None

    def _get_coordinates(self, city: str) -> Optional[Dict]:
        """
        Get coordinates for a city name using geocoding API
        """
        try:
            params = {
                'q': city,
                'limit': 1,
                'appid': self.api_key
            }

            response = requests.get(f"{self.GEO_URL}/direct", params=params)
            response.raise_for_status()

            data = response.json()
            if data:
                return {
                    'lat': data[0]['lat'],
                    'lon': data[0]['lon'],
                    'name_en': data[0]['name']
                }

            return None

        except requests.RequestException as e:
            print(f"Error geocoding city: {e}")
            return None
