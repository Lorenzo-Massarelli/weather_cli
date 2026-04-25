from api import get_weather, get_forecast
from utils import get_city
from services import (
                        format_weather,
                        print_weather,
                        extract_forecast,
                        forecast_stats,
                        print_forecast,
                        print_stats
                    )


def main():
    while True:
        print("\n=== WEATHER APP ===")
        print("1. Get current weather")
        print("2. Forecast analysis")
        print("0. Exit")
        
        choice=input("Choose an option: ")
        
        if choice == "1":
            city = get_city()
            data = get_weather(city)

            if data:
                weather = format_weather(data)
                print_weather(weather)
            else:
                print("No data found!!!")
        
        
        elif choice == "2":
            city = get_city()
            data = get_forecast(city)
            
            if data:
               forecast_data = extract_forecast(data)
               stats = forecast_stats(forecast_data)
               
               print_forecast(forecast_data)
               print_stats(stats)
               
            else:
                print("Error fetching forecast")
                
                
        elif choice == "0":
            print("Bye!")
            break
        
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()