"""
Weather Analytics Israel Package
Advanced weather analysis application for Israel
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .weather_api import WeatherAPI
from .data_analysis import WeatherAnalyzer
from .visualizations import WeatherVisualizations

__all__ = ['WeatherAPI', 'WeatherAnalyzer', 'WeatherVisualizations']
