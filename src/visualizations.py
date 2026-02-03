"""
Visualization Module
Creates interactive charts and graphs using Plotly
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
from typing import Dict, List


class WeatherVisualizations:
    """Class for creating weather-related visualizations"""

    # Color scheme
    COLORS = {
        'primary': '#1f77b4',
        'secondary': '#ff7f0e',
        'success': '#2ca02c',
        'danger': '#d62728',
        'warning': '#ff9800',
        'info': '#17a2b8'
    }

    @staticmethod
    def create_temperature_gauge(current_temp: float, min_temp: float = -10, max_temp: float = 45) -> go.Figure:
        """
        Create a temperature gauge chart

        Args:
            current_temp: Current temperature
            min_temp: Minimum temperature for scale
            max_temp: Maximum temperature for scale

        Returns:
            Plotly figure
        """
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=current_temp,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Current Temperature (°C)", 'font': {'size': 24}},
            gauge={
                'axis': {'range': [min_temp, max_temp], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [min_temp, 10], 'color': '#e3f2fd'},
                    {'range': [10, 20], 'color': '#90caf9'},
                    {'range': [20, 30], 'color': '#ffcc80'},
                    {'range': [30, max_temp], 'color': '#ff8a65'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': current_temp
                }
            }
        ))

        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=70, b=20),
            font={'family': 'Arial, sans-serif'}
        )

        return fig

    @staticmethod
    def create_forecast_chart(forecast_data: Dict) -> go.Figure:
        """
        Create forecast temperature chart

        Args:
            forecast_data: Forecast data from API

        Returns:
            Plotly figure
        """
        if not forecast_data or 'list' not in forecast_data:
            return go.Figure()

        # Extract data
        dates = [datetime.fromtimestamp(item['dt']) for item in forecast_data['list']]
        temps = [item['main']['temp'] for item in forecast_data['list']]
        feels_like = [item['main']['feels_like'] for item in forecast_data['list']]
        humidity = [item['main']['humidity'] for item in forecast_data['list']]

        # Create figure with secondary y-axis
        fig = make_subplots(
            rows=2, cols=1,
            row_heights=[0.7, 0.3],
            subplot_titles=('Temperature Forecast', 'Relative Humidity (%)'),
            vertical_spacing=0.15
        )

        # Temperature traces
        fig.add_trace(
            go.Scatter(
                x=dates, y=temps,
                name='Temperature',
                line=dict(color=WeatherVisualizations.COLORS['primary'], width=3),
                mode='lines+markers'
            ),
            row=1, col=1
        )

        fig.add_trace(
            go.Scatter(
                x=dates, y=feels_like,
                name='Feels Like',
                line=dict(color=WeatherVisualizations.COLORS['secondary'], width=2, dash='dot'),
                mode='lines'
            ),
            row=1, col=1
        )

        # Humidity trace
        fig.add_trace(
            go.Scatter(
                x=dates, y=humidity,
                name='Humidity',
                fill='tozeroy',
                line=dict(color=WeatherVisualizations.COLORS['info'], width=2),
                mode='lines'
            ),
            row=2, col=1
        )

        fig.update_xaxes(title_text="Date and Time", row=2, col=1)
        fig.update_yaxes(title_text="Temperature (°C)", row=1, col=1)
        fig.update_yaxes(title_text="Humidity (%)", row=2, col=1)

        fig.update_layout(
            height=600,
            hovermode='x unified',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(l=50, r=50, t=80, b=50)
        )

        return fig

    @staticmethod
    def create_daily_forecast_chart(forecast_data: Dict) -> go.Figure:
        """
        Create daily forecast chart with highs/lows and weather icons
        Similar to iPhone weather app

        Args:
            forecast_data: Forecast data from API

        Returns:
            Plotly figure with daily highs/lows
        """
        if not forecast_data or 'list' not in forecast_data:
            return go.Figure()

        from collections import defaultdict

        # Group forecasts by day
        daily_data = defaultdict(lambda: {'temps': [], 'weather': [], 'date': None})

        for item in forecast_data['list']:
            dt = datetime.fromtimestamp(item['dt'])
            day_key = dt.strftime('%Y-%m-%d')

            daily_data[day_key]['temps'].append(item['main']['temp'])
            daily_data[day_key]['weather'].append(item['weather'][0]['main'])
            if daily_data[day_key]['date'] is None:
                daily_data[day_key]['date'] = dt

        # Process daily data
        days = []
        day_names = []
        highs = []
        lows = []
        weather_icons = []

        # Weather emoji mapping
        weather_emoji = {
            'Clear': '☀️',
            'Clouds': '☁️',
            'Rain': '🌧️',
            'Drizzle': '🌦️',
            'Thunderstorm': '⛈️',
            'Snow': '❄️',
            'Mist': '🌫️',
            'Smoke': '🌫️',
            'Haze': '🌫️',
            'Dust': '🌫️',
            'Fog': '🌫️',
            'Sand': '🌫️',
            'Ash': '🌫️',
            'Squall': '💨',
            'Tornado': '🌪️'
        }

        for day_key in sorted(daily_data.keys())[:5]:  # Get up to 5 days
            data = daily_data[day_key]
            dt = data['date']

            # Determine day name
            if dt.date() == datetime.now().date():
                day_name = 'Today'
            elif dt.date() == (datetime.now().date() + __import__('datetime').timedelta(days=1)):
                day_name = 'Tomorrow'
            else:
                day_name = dt.strftime('%a')  # Mon, Tue, etc.

            # Get most common weather condition
            most_common = max(set(data['weather']), key=data['weather'].count)
            icon = weather_emoji.get(most_common, '🌤️')

            days.append(dt.strftime('%m/%d'))
            day_names.append(day_name)
            highs.append(max(data['temps']))
            lows.append(min(data['temps']))
            weather_icons.append(f"{icon}")

        # Create figure
        fig = go.Figure()

        # Add high temperatures
        fig.add_trace(go.Bar(
            x=day_names,
            y=highs,
            name='High',
            marker_color='#ff8a65',
            text=[f"{h:.1f}°C" for h in highs],
            textposition='outside',
            textfont=dict(size=14, color='#d84315')
        ))

        # Add low temperatures
        fig.add_trace(go.Bar(
            x=day_names,
            y=lows,
            name='Low',
            marker_color='#90caf9',
            text=[f"{l:.1f}°C" for l in lows],
            textposition='inside',
            textfont=dict(size=14, color='#0d47a1')
        ))

        # Add weather icons as annotations
        for i, (day, icon) in enumerate(zip(day_names, weather_icons)):
            fig.add_annotation(
                x=i,
                y=max(highs) + 3,
                text=icon,
                showarrow=False,
                font=dict(size=30)
            )

        fig.update_layout(
            title='5-Day Forecast',
            xaxis_title='',
            yaxis_title='Temperature (°C)',
            barmode='group',
            height=400,
            margin=dict(l=50, r=50, t=100, b=50),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            plot_bgcolor='rgba(240,240,240,0.5)',
            yaxis=dict(gridcolor='rgba(200,200,200,0.3)')
        )

        return fig

    @staticmethod
    def create_weather_metrics_chart(weather_data: Dict) -> go.Figure:
        """
        Create comprehensive weather metrics chart

        Args:
            weather_data: Current weather data

        Returns:
            Plotly figure
        """
        if not weather_data or 'main' not in weather_data:
            return go.Figure()

        # Extract metrics
        metrics = {
            'Humidity': weather_data['main'].get('humidity', 0),
            'Atmospheric\nPressure\n(hPa)': weather_data['main'].get('pressure', 0) / 10,  # Scale down for visualization
            'Wind Speed\n(m/s)': weather_data['wind'].get('speed', 0),
            'Cloudiness\n(%)': weather_data['clouds'].get('all', 0)
        }

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=list(metrics.values()),
            theta=list(metrics.keys()),
            fill='toself',
            line_color=WeatherVisualizations.COLORS['primary'],
            fillcolor='rgba(31, 119, 180, 0.3)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            title="Weather Metrics",
            height=400,
            margin=dict(l=80, r=80, t=80, b=50)
        )

        return fig

    @staticmethod
    def create_heat_index_chart(temp_range: List[float], humidity: float) -> go.Figure:
        """
        Create heat index comparison chart

        Args:
            temp_range: Range of temperatures
            humidity: Humidity percentage

        Returns:
            Plotly figure
        """
        from src.data_analysis import WeatherAnalyzer

        temps = temp_range
        heat_indices = []

        for temp in temps:
            hi = WeatherAnalyzer.calculate_heat_index(temp, humidity)
            heat_indices.append(hi['heat_index'])

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=temps,
            y=temps,
            name='Actual Temperature',
            line=dict(color=WeatherVisualizations.COLORS['primary'], width=2, dash='dash'),
            mode='lines'
        ))

        fig.add_trace(go.Scatter(
            x=temps,
            y=heat_indices,
            name='Feels Like (Heat Index)',
            line=dict(color=WeatherVisualizations.COLORS['danger'], width=3),
            mode='lines+markers',
            fill='tonexty',
            fillcolor='rgba(214, 39, 40, 0.1)'
        ))

        fig.update_layout(
            title=f"Effect of Humidity on Heat Perception (Humidity: {humidity}%)",
            xaxis_title="Actual Temperature (°C)",
            yaxis_title="Perceived Temperature (°C)",
            height=400,
            margin=dict(l=50, r=50, t=80, b=50),
            hovermode='x unified'
        )

        return fig
