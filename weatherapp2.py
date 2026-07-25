
import random


weather = {
    "baku": "Sunny",
    "moscow": "Rainy",
    "istanbul": "Cloudy",
    "paris": "Windy",
    "london": "Foggy"
}



history = []


possible_weather = ["Sunny", "Rainy", "Cloudy", "Windy", "Foggy", "Snowy", "Stormy"]

while True:
    city = input("Seher daxil edin ('exit' cixis ucun): ").lower()

    if city.lower() == "exit":
        break

    
    if city not in weather:
        forecast = random.choice(possible_weather)
        weather[city] = forecast
        print(f"Yeni seher daxil edildi: {city} → {forecast}")
    else:
        forecast = weather[city]
        print(f" {city} → {forecast}")

    
    history.append((city, forecast))


print("\n Tarixce:")
for i, (city, forecast) in enumerate(history, start=1):
    print(f"{i}. {city} → {forecast}")
