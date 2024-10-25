# Real-Time Weather Monitoring System with Rollups and Aggregates

## Objective
This real-time data processing system retrieves weather data for major Indian cities from the OpenWeatherMap API and generates daily summaries, rollups, and alerts based on predefined thresholds.

## Features
- Real-time data retrieval from OpenWeatherMap API
- Continuous weather monitoring with user-configurable intervals
- Temperature conversion from Kelvin to Celsius or Fahrenheit
- Rollup calculations for daily summaries (average, min, max temperature)
- Alerting system based on thresholds (e.g., temperature exceeds 35°C)
- Visualizations for daily summaries and alerts

## Requirements
- Python 3.8+
- MySQL or SQLite for data storage
- Flask (for web visualization)
- OpenWeatherMap API key (sign up at [OpenWeatherMap](https://openweathermap.org/))

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/weather-monitoring-system.git
