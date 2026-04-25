# Weather CLI App

A Python command-line application that fetches real-time weather data and forecasts using the OpenWeatherMap API, processes the data, and displays clean, readable output.

---

## Architecture
- main.py → CLI controller (menu & flow)
- api.py → API requests (OpenWeatherMap)
- services.py → data processing & formatting
- utils.py → input handling
- requirements.txt
- README.md



## Features
- Get current weather for any city
- 5-day forecast (3-hour intervals)
- Temperature analysis (min, max, average)
- Modular architecture (API, services, CLI separation)
- Secure API key management via environment variables



## How to run
- 1. Clone the repository:
  ```bash
  git clone https://github.com/your-username/weather-cli.git
  cd weather-cli

- 2.Install dependencies
  ```bash
  pip install -r requirements.txt

- 3.Set API key:
  (Windows)
  ```bash
  set OPENWEATHER_API_KEY=your_api_key

  (macOS / Linux)
  ```bash
  export OPENWEATHER_API_KEY=your_api_key

- 3.Run:
  python main.py



## Example
1.Current Weather
--- CURRENT WEATHER ---
City: Rome
Temperature: 18 °C
Feels like: 17 °C
Humidity: 60 %
Condition: clear sky

2.Forecast
--- FORECAST ---
2024-04-20 12:00 → 19 °C
2024-04-20 15:00 → 21 °C
...

3.Statistics
--- STATISTICS ---
Min: 14
Max: 22
Avg: 18.6



## API Used
- https://api.openweathermap.org/data/2.5



## Author
Lorenzo Massarelli