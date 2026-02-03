# 📁 Project Files Overview

Quick guide to what each file does.

---

## 🎯 Main Files

### `main.py` ⭐
**Main Application**
- Complete Streamlit application
- 4 interactive tabs
- English user interface
- ~245 lines of code
- **This is what you run!** (`streamlit run main.py`)
- Contains 3 functions: `get_api_key()`, `create_weather_map()`, `main()`

---

## 📚 src/ Directory - Source Code

### `src/weather_api.py`
**API Module**
- Class: `WeatherAPI`
- Integration with OpenWeatherMap API
- Methods:
  - `__init__(api_key)` - Initializes API client
  - `get_current_weather()` - Fetches current weather data
  - `get_forecast()` - Fetches 5-day forecast
  - `_get_coordinates()` - Private method for geocoding city names
- Uses geocoding API to convert city names to coordinates
- ~123 lines of code

### `src/data_analysis.py`
**Data Analysis Module**
- Class: `WeatherAnalyzer`
- Trend analysis and data from API
- Static methods:
  - `analyze_forecast_trends()` - Forecast trend analysis
  - `calculate_heat_index()` - Heat Index calculation
- ~113 lines of code

### `src/visualizations.py`
**Visualizations Module**
- Class: `WeatherVisualizations`
- Chart creation with Plotly
- Static methods (4 chart types):
  - `create_temperature_gauge()` - Temperature gauge chart
  - `create_forecast_chart()` - Multi-panel forecast chart
  - `create_weather_metrics_chart()` - Radar chart for metrics
  - `create_heat_index_chart()` - Heat index comparison chart
- ~243 lines of code

### `src/__init__.py`
**Package Initialization File**
- Defines src as a Python package
- Imports all classes
- Version information

---

## 📋 Configuration Files

### `requirements.txt`
**Python Dependencies**
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
- Used for `pip install -r requirements.txt`

### `pyproject.toml`
**Poetry Settings**
- Project name and version
- **Important**: `package-mode = false` for Streamlit
- Compatible with PyCharm and IDEs

### `.gitignore`
**Files Not to Upload to Git**
- `secrets.toml` - API keys
- `__pycache__/` - Python cache
- `venv/` - Virtual environment
- IDE files

---

## 🔐 .streamlit/ Directory

### `.streamlit/secrets.toml.example`
**Secrets File Example**
```toml
api_key = "YOUR_OPENWEATHERMAP_API_KEY_HERE"
```
- Copy to `secrets.toml` and enter your key

### `.streamlit/secrets.toml`
**Your Secrets File** ⚠️
- **Does not exist by default!** You need to create it
- Contains your API key
- **Not uploaded to Git** (because of .gitignore)
- Format:
  ```toml
  api_key = "your_actual_api_key_here"
  ```

---

## 📖 Guides

### `QUICKSTART.md` ⚡
**Quick Start**
- 3 simple steps
- Run in 5 minutes
- Common issues
- For those who want to start quickly

### `README.md` 📚
**Full Documentation**
- Project description
- Detailed installation
- Usage instructions
- Technologies

### `FILES_OVERVIEW.md` 📁
**This guide!**
- What each file does
- Where to find what

---

## 🗂️ Full Structure

```
weather_analytics_israel/
│
├── 🎯 main.py                         [245 lines] - Main application
│
├── 📁 src/                            [479+ lines] - Source code
│   ├── __init__.py                    [13 lines]
│   ├── weather_api.py                 [123 lines]
│   ├── data_analysis.py                [113 lines]
│   └── visualizations.py               [243 lines]
│
├── 📁 .streamlit/                     - Streamlit settings
│   ├── secrets.toml.example           [3 lines]
│   └── secrets.toml                   [Need to create!]
│
├── 📚 Guides:
│   ├── QUICKSTART.md
│   ├── README.md
│   └── FILES_OVERVIEW.md              [You are here]
│
└── ⚙️ Configuration files:
    ├── requirements.txt               [8 packages]
    ├── pyproject.toml                 [Poetry config]
    ├── .gitignore                     [Python patterns]
    └── LICENSE                        [MIT]
```

---

## 📊 Statistics

- **Python code**: ~724 lines
- **Guides**: 3 files
- **Modules**: 4 (main + 3 src modules)
- **Classes**: 3
- **Functions/Methods**: 9 total
- **Dependencies**: 8 (pandas and python-dotenv in requirements but not used in code)
- **Chart types**: 4

---

## 🎯 Important Files by Role

### For Beginners:
1. `QUICKSTART.md` - Quick start guide
2. `README.md` - Full documentation

### For Developers:
1. `main.py` - Main code
2. `src/` - All modules

### For Deployment:
1. `.gitignore` - Protecting secrets
2. `requirements.txt` - Dependencies
3. `README.md` - Deployment section

### For Reading:
1. `README.md` - Full documentation
2. `FILES_OVERVIEW.md` - This guide

---

## 💡 Tips

### For Editing:
- **main.py**: User interface and UI
- **src/weather_api.py**: Add API endpoints
- **src/data_analysis.py**: Add analyses
- **src/visualizations.py**: Add charts

### For Reading:
- Start with `QUICKSTART.md` or `README.md`
- Read the code in `src/`

### For Sharing:
- Upload to GitHub
- Deploy to Streamlit Cloud
- Share the URL

---

---

## 📚 Detailed Function Reference

### main.py Functions

#### `get_api_key()`
**Purpose**: Retrieves the OpenWeatherMap API key from Streamlit secrets or prompts the user to enter it manually.

**How it works**:
1. First tries to access `st.secrets["api_key"]` from `.streamlit/secrets.toml`
2. If not found, displays a warning and shows a password input field in the sidebar
3. If user enters a key, returns it
4. If no key is provided, displays instructions and stops the app

**Returns**: `str` - The API key string

**Error handling**: Catches exceptions when secrets file doesn't exist

---

#### `create_weather_map(lat, lon, city_name, weather_condition)`
**Purpose**: Creates an interactive Folium map with a weather marker at the specified location.

**Parameters**:
- `lat` (float): Latitude coordinate
- `lon` (float): Longitude coordinate
- `city_name` (str): Name of the city to display
- `weather_condition` (str): Weather description to show in popup

**How it works**:
1. Creates a Folium Map centered at the given coordinates with zoom level 10
2. Adds a blue cloud icon marker at the location
3. Sets popup text with city name and weather condition
4. Returns the map object for display in Streamlit

**Returns**: `folium.Map` - Interactive map object

---

#### `main()`
**Purpose**: Main application entry point that orchestrates the entire UI and data flow.

**How it works**:
1. **Initialization**: Gets API key and creates WeatherAPI instance
2. **Sidebar Setup**: Creates city input field in sidebar
3. **Data Fetching**: When city is entered:
   - Calls `get_current_weather()` to get current conditions
   - Calls `get_forecast()` to get 5-day forecast
   - Extracts temperature, humidity, pressure, wind, description, coordinates
4. **UI Creation**: Creates 4 tabs:
   - **Tab 1 (Current Status)**: Shows metrics, temperature gauge, weather metrics radar chart
   - **Tab 2 (Forecast)**: Shows forecast trends, averages, rain probability, forecast chart
   - **Tab 3 (Heat Index)**: Shows heat index calculation and chart
   - **Tab 4 (Map)**: Shows interactive map with weather marker
5. **Error Handling**: Stops app if weather data cannot be loaded

**Data Flow**: API → Extract Data → Analysis → Visualization → Display

---

### WeatherAPI Class Methods

#### `__init__(api_key)`
**Purpose**: Initializes the WeatherAPI class with an API key.

**Parameters**:
- `api_key` (str): OpenWeatherMap API key

**How it works**: Stores the API key as an instance variable for use in all API requests.

---

#### `get_current_weather(city=None, lat=None, lon=None)`
**Purpose**: Fetches current weather data for a location using either city name or coordinates.

**Parameters**:
- `city` (str, optional): City name (any language)
- `lat` (float, optional): Latitude
- `lon` (float, optional): Longitude

**How it works**:
1. If city is provided, calls `_get_coordinates()` to convert city name to lat/lon
2. If coordinates not found, returns None
3. Makes GET request to `/weather` endpoint with:
   - lat, lon coordinates
   - API key
   - units: metric (Celsius)
   - lang: en (English descriptions)
4. Returns JSON response with weather data
5. Handles errors gracefully, prints error message, returns None

**Returns**: `Dict` with weather data or `None` on error

**Data returned includes**: temperature, humidity, pressure, wind speed, weather description, coordinates

---

#### `get_forecast(city=None, lat=None, lon=None, days=5)`
**Purpose**: Fetches 5-day weather forecast data for a location.

**Parameters**:
- `city` (str, optional): City name
- `lat` (float, optional): Latitude
- `lon` (float, optional): Longitude
- `days` (int): Number of days (default 5, max 5 for free tier)

**How it works**:
1. If city provided, gets coordinates via `_get_coordinates()`
2. Makes GET request to `/forecast` endpoint
3. Sets `cnt` parameter to `days * 8` (8 forecasts per day, every 3 hours)
4. Returns forecast data with list of forecast points
5. Handles errors, returns None on failure

**Returns**: `Dict` with forecast list or `None` on error

**Forecast data**: Contains list of forecast objects, each with temperature, humidity, weather conditions, timestamps

---

#### `_get_coordinates(city)`
**Purpose**: Private method that converts a city name to latitude and longitude using geocoding API.

**Parameters**:
- `city` (str): City name in any language

**How it works**:
1. Makes GET request to geocoding API (`/geo/1.0/direct`)
2. Searches for city name with limit=1 (first result)
3. Extracts lat, lon, and English name from response
4. Returns dictionary with coordinates and name
5. Returns None if city not found or on error

**Returns**: `Dict` with `lat`, `lon`, `name_en` or `None`

**Note**: This is a private method (starts with `_`) used internally by other methods

---

### WeatherAnalyzer Class Methods

#### `analyze_forecast_trends(forecast_data)`
**Purpose**: Analyzes forecast data to determine temperature trends, calculate statistics, and estimate rain probability.

**Parameters**:
- `forecast_data` (Dict): Forecast data dictionary from API

**How it works**:
1. **Validation**: Checks if forecast_data exists and has 'list' key
2. **Temperature Extraction**: Extracts all temperature values from forecast list
3. **Statistics Calculation**:
   - Average temperature using numpy.mean()
   - Minimum and maximum temperatures
4. **Trend Detection**:
   - Calculates average of first 8 forecasts (first 24 hours)
   - Calculates average of last 8 forecasts (last 24 hours)
   - Compares to determine if trend is "Rising" or "Falling"
   - Calculates difference
5. **Rain Probability**:
   - Counts how many forecast points have 'rain' key
   - Calculates percentage
6. Returns dictionary with all calculated metrics

**Returns**: `Dict` with:
- `has_data`: Boolean
- `avg_temp`, `min_temp`, `max_temp`: Temperature statistics
- `trend`: "Rising" or "Falling"
- `trend_diff`: Temperature difference
- `rain_probability`: Percentage
- `num_forecasts`: Total number of forecast points

---

#### `calculate_heat_index(temp_c, humidity)`
**Purpose**: Calculates the heat index (feels-like temperature) using Steadman's formula, which combines actual temperature and humidity.

**Parameters**:
- `temp_c` (float): Temperature in Celsius
- `humidity` (float): Relative humidity (0-100)

**How it works**:
1. **Conversion**: Converts Celsius to Fahrenheit (formula requires Fahrenheit)
2. **Simplified Formula**: First calculates simplified heat index
3. **Full Formula**: If result >= 80°F, uses the complete Steadman's formula with multiple coefficients
4. **Conversion Back**: Converts result back to Celsius
5. **Comfort Analysis**: Calculates difference between heat index and actual temperature
6. **Comfort Level Determination**:
   - Difference < 2°C: "Comfortable"
   - Difference < 4°C: "Slightly Uncomfortable"
   - Difference < 6°C: "Uncomfortable"
   - Difference >= 6°C: "Dangerous"
7. Returns dictionary with heat index, comfort level, emoji, and description

**Returns**: `Dict` with:
- `heat_index`: Calculated heat index in Celsius
- `actual_temp`: Original temperature
- `difference`: Difference between heat index and actual temp
- `comfort`: Comfort level string
- `emoji`: Emoji for comfort level
- `description`: Text description

**Formula**: Uses Steadman's heat index formula which accounts for temperature and humidity interaction

---

### WeatherVisualizations Class Methods

#### `create_temperature_gauge(current_temp, min_temp=-10, max_temp=45)`
**Purpose**: Creates an interactive gauge chart showing current temperature with color-coded ranges.

**Parameters**:
- `current_temp` (float): Current temperature to display
- `min_temp` (float): Minimum scale value (default -10°C)
- `max_temp` (float): Maximum scale value (default 45°C)

**How it works**:
1. Creates Plotly Indicator chart in gauge mode
2. Sets value to current temperature
3. Configures gauge with:
   - Color-coded steps: Blue (cold), Light blue (cool), Orange (warm), Red (hot)
   - Reference line at 20°C for comparison
   - Custom styling and layout
4. Returns figure for Streamlit display

**Returns**: `go.Figure` - Plotly figure object

---

#### `create_forecast_chart(forecast_data)`
**Purpose**: Creates a multi-panel chart showing temperature forecast and humidity over time.

**Parameters**:
- `forecast_data` (Dict): Forecast data from API

**How it works**:
1. **Data Extraction**: Extracts dates, temperatures, feels-like temps, and humidity from forecast list
2. **Subplot Creation**: Creates 2-row subplot:
   - Top row (70%): Temperature forecast
   - Bottom row (30%): Humidity chart
3. **Temperature Traces**:
   - Main temperature line (blue, solid)
   - Feels-like temperature line (orange, dashed)
4. **Humidity Trace**: Filled area chart showing humidity percentage
5. **Layout**: Configures axes, legends, hover mode
6. Returns interactive chart

**Returns**: `go.Figure` - Multi-panel Plotly figure

---

#### `create_weather_metrics_chart(weather_data)`
**Purpose**: Creates a radar/spider chart showing multiple weather metrics in one visualization.

**Parameters**:
- `weather_data` (Dict): Current weather data from API

**How it works**:
1. **Metric Extraction**: Extracts 4 metrics:
   - Humidity (%)
   - Atmospheric Pressure (scaled down by 10 for visualization)
   - Wind Speed (m/s)
   - Cloudiness (%)
2. **Polar Chart**: Creates Scatterpolar chart (radar/spider chart)
3. **Visualization**: Fills area between center and metric values
4. **Layout**: Configures polar coordinates with 0-100 range
5. Returns radar chart

**Returns**: `go.Figure` - Polar/radar chart figure

---

#### `create_heat_index_chart(temp_range, humidity)`
**Purpose**: Creates a comparison chart showing how heat index changes with temperature at a given humidity level.

**Parameters**:
- `temp_range` (List[float]): Range of temperatures to calculate
- `humidity` (float): Humidity percentage (constant for all calculations)

**How it works**:
1. **Heat Index Calculation**: For each temperature in range:
   - Calls `WeatherAnalyzer.calculate_heat_index()` for each temp
   - Stores heat index values
2. **Two Traces**:
   - Dashed line: Actual temperature (y=x line)
   - Solid line: Heat index (shows how humidity affects perception)
3. **Visualization**: Fills area between lines to show difference
4. **Layout**: Configures titles, axes, hover mode
5. Returns comparison chart

**Returns**: `go.Figure` - Comparison chart figure

**Purpose**: Visualizes how humidity makes it feel warmer than actual temperature

---

## 🔄 Application Flow

```
User Input (City Name)
    ↓
get_api_key() → API Key
    ↓
WeatherAPI.__init__(api_key)
    ↓
main() function starts
    ↓
User enters city name
    ↓
WeatherAPI.get_current_weather(city)
    ├─→ _get_coordinates(city) → lat/lon
    └─→ API call → Current weather data
    ↓
WeatherAPI.get_forecast(city)
    ├─→ _get_coordinates(city) → lat/lon
    └─→ API call → Forecast data
    ↓
Extract: temp, humidity, pressure, wind, etc.
    ↓
WeatherAnalyzer.analyze_forecast_trends(forecast)
    └─→ Returns trends, averages, rain probability
    ↓
WeatherAnalyzer.calculate_heat_index(temp, humidity)
    └─→ Returns heat index, comfort level
    ↓
WeatherVisualizations methods
    ├─→ create_temperature_gauge()
    ├─→ create_forecast_chart()
    ├─→ create_weather_metrics_chart()
    └─→ create_heat_index_chart()
    ↓
Display in Streamlit UI (4 tabs)
```

---

**Now you know where everything is and how it works! 🎉**

Back to [README.md](README.md)
