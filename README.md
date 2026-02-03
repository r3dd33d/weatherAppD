# 🌤️ Weather Analytics

**Advanced real-time weather analysis application with interactive visualizations**

A Python-based weather analytics platform that provides comprehensive weather data, forecasts, and advanced metrics using the OpenWeatherMap API. Built with Streamlit for an intuitive, interactive user experience.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

### 🌍 **Multi-language City Search**
- Search for any city worldwide in **any language** (Hebrew, Arabic, English, etc.)
- Automatic geocoding converts city names to coordinates
- Smart display shows city name in English with original language in parentheses

### 📊 **Current Weather Dashboard**
- Real-time temperature, humidity, wind speed, and atmospheric pressure
- Interactive temperature gauge with color-coded zones
- Weather description and conditions
- 5-day forecast cards with daily high/low temperatures and weather icons

### 📈 **Forecast & Trend Analysis**
- 5-day weather forecast with 3-hour intervals
- Automatic trend detection (rising/falling temperatures)
- Statistical analysis: average, minimum, maximum temperatures
- Rain probability calculations
- Interactive multi-panel charts

### 🔥 **Heat Index Analysis**
- Advanced heat index calculation using Steadman's formula
- Comfort level assessment (Comfortable, Slightly Uncomfortable, Uncomfortable, Dangerous)
- Temperature perception analysis based on humidity
- Interactive comparison charts

### 🗺️ **Interactive Maps**
- Location-based weather visualization
- Interactive map with weather markers
- City identification with coordinates

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.9 or higher**
- **OpenWeatherMap API key** (free tier available)
- **Git** (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/r3dd33d/weatherAppD
   cd weather-analytics
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv

   # Activate on Windows:
   venv\Scripts\activate

   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**

   Create a `.streamlit/secrets.toml` file:
   ```bash
   mkdir -p .streamlit
   touch .streamlit/secrets.toml
   ```

   Add your API key to the file:
   ```toml
   api_key = "YOUR_OPENWEATHERMAP_API_KEY"
   ```

   **Get your free API key:**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Navigate to **API keys** section
   - Copy your generated API key

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

   The application will open automatically in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
weather-analytics/
│
├── main.py                      # Main Streamlit application
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Poetry configuration
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
│
├── .streamlit/
│   └── secrets.toml            # API key configuration (not in Git)
│
└── src/
    ├── __init__.py             # Package initialization
    ├── weather_api.py          # OpenWeatherMap API integration
    ├── data_analysis.py        # Weather data analysis and calculations
    └── visualizations.py       # Plotly chart generation
```

---

## 🛠️ Technologies

### Core
- **Python 3.9+** - Programming language
- **Streamlit** - Web application framework
- **OpenWeatherMap API** - Real-time weather data source

### Data & Analysis
- **NumPy** - Numerical computations and statistical analysis
- **Requests** - HTTP library for API calls

### Visualization
- **Plotly** - Interactive charts and graphs
- **Folium** - Interactive maps
- **streamlit-folium** - Folium integration for Streamlit

---

## 📊 Application Modules

### `main.py` - Main Application
- Streamlit UI orchestration
- User input handling
- Tab management (Current Status, Forecast, Heat Index, Map)
- Data flow coordination

### `src/weather_api.py` - API Integration
**Class:** `WeatherAPI`

- `get_current_weather()` - Fetches current weather data
- `get_forecast()` - Retrieves 5-day forecast (40 data points)
- `_get_coordinates()` - Geocoding for city name to coordinates conversion

### `src/data_analysis.py` - Data Analysis
**Class:** `WeatherAnalyzer`

- `analyze_forecast_trends()` - Statistical analysis of forecast data
  - Average, min, max temperatures
  - Trend detection (rising/falling)
  - Rain probability calculation

- `calculate_heat_index()` - Heat index computation
  - Steadman's formula implementation
  - Comfort level assessment
  - Temperature perception analysis

### `src/visualizations.py` - Visualizations
**Class:** `WeatherVisualizations`

- `create_temperature_gauge()` - Temperature gauge with color zones
- `create_forecast_chart()` - Multi-panel forecast visualization
- `create_heat_index_chart()` - Heat index comparison chart
- `create_daily_forecast_chart()` - Daily forecast with highs/lows

---

## 🎨 Features in Detail

### Daily Forecast Cards

The application displays weather forecasts as beautiful, easy-to-read cards:

- **Day identification**: "Today (Mon)", "Tomorrow (Tue)", "Wed", etc.
- **Large weather emoji**: Visual representation of conditions (☀️, ☁️, 🌧️, ❄️, etc.)
- **Temperature display**: High temperature (large, orange) and low temperature (smaller, blue)
- **Date stamps**: Month/day format for clarity
- **Gradient backgrounds**: Visually appealing purple-to-blue gradients

### Heat Index Calculation

Advanced comfort analysis combining temperature and humidity:

```
Heat Index = f(Temperature, Humidity)

Comfort Levels:
- Difference < 2°C: Comfortable 😊
- Difference < 4°C: Slightly Uncomfortable 😐
- Difference < 6°C: Uncomfortable 😓
- Difference ≥ 6°C: Dangerous 🥵
```

### Trend Analysis

Intelligent forecast analysis:
- Compares first 24 hours vs. last 24 hours of forecast
- Identifies temperature trends (rising/falling)
- Calculates statistical measures
- Estimates rain probability based on forecast data

---

## 🌐 API Information

### OpenWeatherMap API Usage

**Endpoints used:**
- **Geocoding API**: `https://api.openweathermap.org/geo/1.0/direct`
  - Converts city names to coordinates
  - Supports multiple languages

- **Current Weather API**: `https://api.openweathermap.org/data/2.5/weather`
  - Real-time weather data
  - Temperature, humidity, pressure, wind speed

- **Forecast API**: `https://api.openweathermap.org/data/2.5/forecast`
  - 5-day forecast (3-hour intervals)
  - 40 data points total

**API Limits (Free Tier):**
- 1,000 calls per day
- 60 calls per minute

---

## ⚙️ Configuration

### Secrets Management

The application uses Streamlit's secrets management for secure API key storage.

**File:** `.streamlit/secrets.toml`
```toml
api_key = "your_openweathermap_api_key_here"
```

**Security notes:**
- ✅ `.streamlit/secrets.toml` is in `.gitignore` (never committed)
- ✅ API key is never exposed in the codebase
- ✅ Fallback to manual input if secrets file is missing

### Environment Variables (Alternative)

You can also use environment variables:
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

---

## 🚀 Deployment

### Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Visit [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign in with GitHub
   - Click **New app**
   - Select your repository
   - Configure:
     - Main file: `main.py`
     - Python version: 3.9+
   - Add your API key in **Advanced settings** → **Secrets**:
     ```toml
     api_key = "YOUR_API_KEY"
     ```
   - Click **Deploy**

Your app will be live at a unique URL!

---

## 🎯 Usage Examples

### Search for a city in any language

**English:**
```
Enter city name: London
→ Displays: "Advanced Weather Analytics - London"
```

**Hebrew:**
```
Enter city name: תל אביב
→ Displays: "Advanced Weather Analytics - Tel Aviv (תל אביב)"
```

**Arabic:**
```
Enter city name: القاهرة
→ Displays: "Advanced Weather Analytics - Cairo (القاهرة)"
```

### Navigate between tabs

1. **📊 Current Status**: View current conditions and 5-day forecast
2. **📈 Forecast & Analysis**: Detailed trend analysis with charts
3. **🔥 Heat Index**: Comfort analysis based on temperature and humidity
4. **🌍 Map**: Interactive location map

---

## 🧪 Development

### Running in Development Mode

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Run with auto-reload
streamlit run main.py --server.runOnSave true
```

### Code Style

The project follows Python best practices:
- **PEP 8** style guide
- **Type hints** for function signatures
- **Docstrings** for all functions and classes
- **Modular architecture** for maintainability

### Project Statistics

- **Total Lines**: ~724 lines of Python code
- **Modules**: 4 (main + 3 source modules)
- **Functions/Methods**: 9+
- **Visualization Types**: 4
- **Supported Languages**: 100+ (via OpenWeatherMap)

---

## 📝 Requirements

**Python Packages:**
```
streamlit==1.32.0
requests==2.31.0
plotly==5.19.0
folium==0.15.1
streamlit-folium==0.18.0
pandas==2.2.0
numpy==1.26.4
python-dotenv==1.0.1
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) - Excellent weather API
- [Streamlit](https://streamlit.io/) - Powerful web framework for data apps
- [Plotly](https://plotly.com/) - Interactive visualization library
- [Folium](https://python-visualization.github.io/folium/) - Leaflet.js integration

---

## 📧 Contact

**Project Maintainer:** Daniel Zavulunov
**Email:** danielz@law-yal.com

---

## 🌟 Support

If you find this project useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing to the codebase

---

**Built with ❤️ using Python and Streamlit**
