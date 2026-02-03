"""
Data Analysis Module
Handles weather data trends and statistical analysis
"""

import numpy as np
from typing import Dict


class WeatherAnalyzer:
    """Class for analyzing weather data and trends"""

    @staticmethod
    def analyze_forecast_trends(forecast_data: Dict) -> Dict:
        """
        Analyze trends in forecast data

        Args:
            forecast_data: Forecast data from API

        Returns:
            Dictionary with trend analysis
        """
        if not forecast_data or 'list' not in forecast_data:
            return {"has_data": False}

        temps = [item['main']['temp'] for item in forecast_data['list']]

        # Calculate statistics
        avg_temp = np.mean(temps)
        min_temp = min(temps)
        max_temp = max(temps)

        # Find trend (warming or cooling)
        first_day_avg = np.mean(temps[:8])  # First 24 hours
        last_day_avg = np.mean(temps[-8:])  # Last 24 hours
        trend = "Rising" if last_day_avg > first_day_avg else "Falling"
        trend_diff = abs(last_day_avg - first_day_avg)

        # Rain probability
        rain_forecasts = [item for item in forecast_data['list'] if 'rain' in item]
        rain_probability = (len(rain_forecasts) / len(forecast_data['list'])) * 100

        return {
            "has_data": True,
            "avg_temp": round(avg_temp, 1),
            "min_temp": round(min_temp, 1),
            "max_temp": round(max_temp, 1),
            "trend": trend,
            "trend_diff": round(trend_diff, 1),
            "rain_probability": round(rain_probability, 1),
            "num_forecasts": len(temps)
        }

    @staticmethod
    def calculate_heat_index(temp_c: float, humidity: float) -> Dict:
        """
        Calculate heat index (feels like temperature)
        Uses simplified Steadman's formula

        Args:
            temp_c: Temperature in Celsius
            humidity: Relative humidity (0-100)

        Returns:
            Dictionary with heat index info
        """
        # Convert to Fahrenheit for calculation
        temp_f = (temp_c * 9/5) + 32

        # Simplified heat index formula
        hi_f = 0.5 * (temp_f + 61.0 + ((temp_f - 68.0) * 1.2) + (humidity * 0.094))

        # If above threshold, use full formula
        if hi_f >= 80:
            hi_f = (-42.379 + 2.04901523 * temp_f + 10.14333127 * humidity
                    - 0.22475541 * temp_f * humidity - 0.00683783 * temp_f**2
                    - 0.05481717 * humidity**2 + 0.00122874 * temp_f**2 * humidity
                    + 0.00085282 * temp_f * humidity**2 - 0.00000199 * temp_f**2 * humidity**2)

        # Convert back to Celsius
        hi_c = (hi_f - 32) * 5/9

        difference = hi_c - temp_c

        # Determine comfort level
        if difference < 2:
            comfort = "Comfortable"
            emoji = "😊"
            description = "Normal comfort feeling"
        elif difference < 4:
            comfort = "Slightly Uncomfortable"
            emoji = "😐"
            description = "Feeling slightly warmer than actual temperature"
        elif difference < 6:
            comfort = "Uncomfortable"
            emoji = "😓"
            description = "Significant heat load due to humidity"
        else:
            comfort = "Dangerous"
            emoji = "🥵"
            description = "Feeling of heavy heat - limit outdoor activity"

        return {
            "heat_index": round(hi_c, 1),
            "actual_temp": temp_c,
            "difference": round(difference, 1),
            "comfort": comfort,
            "emoji": emoji,
            "description": description
        }

