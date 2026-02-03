"""
Weather Analytics Israel - Main Streamlit Application
Advanced weather analysis app with real-time data from OpenWeatherMap API
"""

import streamlit as st
import folium
from streamlit_folium import folium_static
import sys
from pathlib import Path

# Add src directory to path
sys.path.append(str(Path(__file__).parent))

from src.weather_api import WeatherAPI
from src.data_analysis import WeatherAnalyzer
from src.visualizations import WeatherVisualizations


# Page configuration
st.set_page_config(
    page_title="Weather Analytics - Israel",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)


def get_api_key():
    """Get API key from secrets or allow manual input"""
    try:
        return st.secrets["api_key"]
    except:
        st.sidebar.warning("⚠️ API key not found")
        api_key = st.sidebar.text_input(
            "Enter OpenWeatherMap API Key:",
            type="password",
            help="Get a free API key from https://openweathermap.org/api"
        )
        if api_key:
            return api_key
        else:
            st.info("Create a `.streamlit/secrets.toml` file with: `api_key = \"YOUR_KEY\"`")
            st.stop()


def create_weather_map(lat: float, lon: float, city_name: str, weather_condition: str):
    """Create interactive map with weather marker"""
    m = folium.Map(location=[lat, lon], zoom_start=10)

    # Add marker
    folium.Marker(
        [lat, lon],
        popup=f"{city_name}\n{weather_condition}",
        tooltip=city_name,
        icon=folium.Icon(color='blue', icon='cloud')
    ).add_to(m)

    return m


def main():
    """Main application function"""

    # Get API key
    api_key = get_api_key()
    weather_api = WeatherAPI(api_key)

    # Sidebar
    st.sidebar.header("⚙️ Settings")

    # City selection - using text input with geocoding API
    selected_city = st.sidebar.text_input(
        "Enter city name:",
        value="Tel Aviv",
        help="Enter a city name. The code will use the geocoding API to find the coordinates."
    )

    # Main content
    if selected_city:
        # Get city name in English first
        with st.spinner(f"Loading weather data for {selected_city}..."):
            city_coords = weather_api._get_coordinates(selected_city)
            if not city_coords:
                st.error("❌ City not found. Please check the city name and try again.")
                st.stop()

            city_name_en = city_coords['name_en']

            # Create display name: if input is in a different language, show both
            # Check if the input is in Latin script (English) or different script
            def is_latin(text):
                """Check if text uses primarily Latin characters"""
                return all(ord(char) < 128 or char.isspace() or char in '-,.' for char in text)

            # Only add parentheses if the input is in a different script (not English)
            if not is_latin(selected_city) and selected_city.lower().strip() != city_name_en.lower().strip():
                city_display_name = f"{city_name_en} ({selected_city})"
            else:
                city_display_name = city_name_en

            # Fetch weather data
            current_weather = weather_api.get_current_weather(city=selected_city)
            forecast = weather_api.get_forecast(city=selected_city)

        if not current_weather:
            st.error("❌ Error loading weather data. Check the API key or city name.")
            st.stop()

        # Header with dynamic city name
        st.title(f"🌤️ Advanced Weather Analytics - {city_display_name}")
        st.markdown("### Weather trend analysis application with real-time data")

        # Extract data
        temp = current_weather['main']['temp']
        feels_like = current_weather['main']['feels_like']
        humidity = current_weather['main']['humidity']
        pressure = current_weather['main']['pressure']
        wind_speed = current_weather['wind']['speed']
        description = current_weather['weather'][0]['description']
        lat = current_weather['coord']['lat']
        lon = current_weather['coord']['lon']

        # Create tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Current Status",
            "📈 Forecast & Analysis",
            "🔥 Heat Index",
            "🌍 Map"
        ])

        # Tab 1: Current Weather
        with tab1:
            st.header(f"Current Weather - {city_display_name}")

            # Current conditions
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    label="🌡️ Temperature",
                    value=f"{temp:.1f}°C",
                    delta=f"{temp - feels_like:.1f}°C from feels like"
                )

            with col2:
                st.metric(
                    label="💧 Humidity",
                    value=f"{humidity}%"
                )

            with col3:
                st.metric(
                    label="💨 Wind",
                    value=f"{wind_speed:.1f} m/s"
                )

            with col4:
                st.metric(
                    label="🔽 Pressure",
                    value=f"{pressure} hPa"
                )

            st.markdown(f"**Description:** {description}")

            # Temperature gauge
            st.plotly_chart(
                WeatherVisualizations.create_temperature_gauge(temp),
                use_container_width=True
            )

            # Daily forecast
            st.subheader("📅 5-Day Forecast")

            if forecast and 'list' in forecast:
                from collections import defaultdict
                from datetime import datetime, timedelta

                # Group forecasts by day
                daily_data = defaultdict(lambda: {'temps': [], 'weather': [], 'date': None})

                for item in forecast['list']:
                    dt = datetime.fromtimestamp(item['dt'])
                    day_key = dt.strftime('%Y-%m-%d')

                    daily_data[day_key]['temps'].append(item['main']['temp'])
                    daily_data[day_key]['weather'].append(item['weather'][0]['main'])
                    if daily_data[day_key]['date'] is None:
                        daily_data[day_key]['date'] = dt

                # Weather emoji mapping
                weather_emoji = {
                    'Clear': '☀️', 'Clouds': '☁️', 'Rain': '🌧️', 'Drizzle': '🌦️',
                    'Thunderstorm': '⛈️', 'Snow': '❄️', 'Mist': '🌫️', 'Smoke': '🌫️',
                    'Haze': '🌫️', 'Dust': '🌫️', 'Fog': '🌫️', 'Sand': '🌫️'
                }

                # Create columns for each day (up to 5 days)
                days_to_show = min(5, len(daily_data))
                cols = st.columns(days_to_show)

                for idx, day_key in enumerate(sorted(daily_data.keys())[:days_to_show]):
                    data = daily_data[day_key]
                    dt = data['date']

                    # Determine day name
                    if dt.date() == datetime.now().date():
                        day_name = f'Today ({dt.strftime("%a")})'
                    elif dt.date() == (datetime.now().date() + timedelta(days=1)):
                        day_name = f'Tomorrow ({dt.strftime("%a")})'
                    else:
                        day_name = dt.strftime('%a')

                    # Get most common weather
                    most_common = max(set(data['weather']), key=data['weather'].count)
                    icon = weather_emoji.get(most_common, '🌤️')

                    high = max(data['temps'])
                    low = min(data['temps'])

                    # Display in column
                    with cols[idx]:
                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            padding: 25px;
                            border-radius: 15px;
                            text-align: center;
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                        ">
                            <h3 style="color: white; margin: 0; font-size: 25px; font-weight: 600;">{day_name}</h3>
                            <p style="color: #e0e0e0; margin: 5px 0; font-size: 17px;">{dt.strftime('%m/%d')}</p>
                            <div style="font-size: 70px; margin: 15px 0;">{icon}</div>
                            <p style="color: white; margin: 5px 0; font-size: 20px;">{most_common}</p>
                            <div style="margin-top: 20px;">
                                <p style="color: #ffccbc; margin: 5px 0; font-size: 34px; font-weight: bold;">{high:.1f}°</p>
                                <p style="color: #b3e5fc; margin: 5px 0; font-size: 28px;">{low:.1f}°</p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

        # Tab 2: Forecast and Analysis
        with tab2:
            st.header("Forecast and Trend Analysis")

            if forecast:
                # Trend analysis
                trends = WeatherAnalyzer.analyze_forecast_trends(forecast)

                if trends['has_data']:
                    # Display metrics
                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.metric("🌡️ Average", f"{trends['avg_temp']}°C")

                    with col2:
                        st.metric("❄️ Minimum", f"{trends['min_temp']}°C")

                    with col3:
                        st.metric("🔥 Maximum", f"{trends['max_temp']}°C")

                    with col4:
                        trend_emoji = "📈" if trends['trend'] == "Rising" else "📉"
                        st.metric(
                            f"{trend_emoji} Trend",
                            trends['trend'],
                            f"{trends['trend_diff']:.1f}°C"
                        )

                    # Rain probability
                    if trends['rain_probability'] > 0:
                        st.info(f"🌧️ Rain probability: {trends['rain_probability']:.0f}%")

                    # Forecast chart
                    st.plotly_chart(
                        WeatherVisualizations.create_forecast_chart(forecast),
                        use_container_width=True
                    )
                else:
                    st.warning("No forecast data available")
            else:
                st.error("Unable to load forecast data")

        # Tab 3: Heat Index
        with tab3:
            st.header("🔥 Heat Index and Comfort Analysis")

            heat_data = WeatherAnalyzer.calculate_heat_index(temp, humidity)

            col1, col2 = st.columns([1, 2])

            with col1:
                st.metric(
                    "🌡️ Heat Index",
                    f"{heat_data['heat_index']}°C",
                    f"{heat_data['difference']:+.1f}°C from temperature"
                )

                st.info(f"""
                **Comfort Level:** {heat_data['emoji']} {heat_data['comfort']}

                {heat_data['description']}

                ---

                **Actual Temperature:** {heat_data['actual_temp']}°C

                **Relative Humidity:** {humidity}%
                """)

            with col2:
                # Heat index chart for range of temperatures
                temp_range = list(range(int(temp) - 5, int(temp) + 10))
                st.plotly_chart(
                    WeatherVisualizations.create_heat_index_chart(temp_range, humidity),
                    use_container_width=True
                )

        # Tab 4: Map
        with tab4:
            st.header("🌍 Interactive Map")

            weather_map = create_weather_map(lat, lon, city_name_en, description)
            folium_static(weather_map, width=800, height=500)
    else:
        # Show default message when no city is selected
        st.title("🌤️ Advanced Weather Analytics")
        st.markdown("### Weather trend analysis application with real-time data")
        st.info("👈 Please enter a city name in the sidebar to get started")

if __name__ == "__main__":
    main()
