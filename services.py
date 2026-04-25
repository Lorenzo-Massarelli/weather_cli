def format_weather(data):
    return { 
        "city": data["name"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }

def print_weather(w):
    print("\n--- CURRENT WEATHER ---")
    print(f"City: {w['city']}")
    print(f"Temperature: {w['temp']} °C")
    print(f"Feels like: {w['feels_like']} °C")
    print(f"Humidity: {w['humidity']} %")
    print(f"Condition: {w['description']}")
    
    
    
def extract_forecast(forecast):
    return [
        {
            "time": item["dt_txt"],
            "temp": item["main"]["temp"]
        }
        for item in forecast["list"]
    ]
        


def forecast_stats(data):
    temps = [d["temp"] for d in data]
    return {
            "min": min(temps),
            "max": max(temps),
            "avg": sum(temps) / len(temps)
        }



def print_forecast(data):
    print("\n--- FORECAST ---")
    for d in data[:5]:
        print(f"{d['time']} → {d['temp']} °C")
        
        
        
def print_stats(stats):
    print("\n--- STATISTICS ---")
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")
    print(f"Avg: {round(stats['avg'], 2)}")
    