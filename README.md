# Weather CLI App

A Python command-line application that fetches real-time weather and forecast data using the OpenWeatherMap API, processes it, and displays clean, readable output.

---

## Features

- Get current weather for any city  
- 5-day forecast (3-hour intervals)  
- Temperature analysis (min, max, average)  
- Modular architecture (API, services, CLI separation)  
- Secure API key management via environment variables  

---

## Project Structure

```
weather_cli/
│
├── main.py        # CLI controller (menu & flow)
├── api.py         # API requests
├── services.py    # data processing & formatting
├── utils.py       # input handling
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/TUO_USERNAME/weather_cli.git
cd weather_cli
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set API key

#### Windows
```bash
set OPENWEATHER_API_KEY=your_api_key
```

#### macOS / Linux
```bash
export OPENWEATHER_API_KEY=your_api_key
```

---

## Usage

```bash
python main.py
```

---

## CLI Menu

```
=== WEATHER APP ===
1. Get current weather
2. Forecast analysis
0. Exit
```

---

## Example Output

### Current Weather

```
--- CURRENT WEATHER ---
City: Rome
Temperature: 18 °C
Feels like: 17 °C
Humidity: 60 %
Condition: clear sky
```

---

### Forecast

```
--- FORECAST ---
2024-04-20 12:00 → 19 °C
2024-04-20 15:00 → 21 °C
...
```

---

### Statistics

```
--- STATISTICS ---
Min: 14
Max: 22
Avg: 18.6
```

---

## API Used

- https://api.openweathermap.org/data/2.5

---

## Author

Lorenzo Massarelli
