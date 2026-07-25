import random


weather = {
    "baki" : "gunesli",
    "sumqayit": "buludlu",
    "zerdab": "yagis",
    "goycay": "yagis",
    "zaqatala": "gunesli",
    "qebele": "gunesli",
    "qax": "kulekli",
    "qusar": "Dumanli",
}

#weather["qax"] = 'kulekli'


#unique_weather = set()
history = []

psblewthr = ['kulekli','buludlu','dumanli','yagisli','gunesli' ]


while True:
    city = input(("Seheri secin ('exit' ---> cixis): ")).lower()
    if city == 'exit':
        break
    elif city in weather:
        print(f'{city.title()} ━━━> {weather[city]} hava durumu')
        forecast=""
        history.append((city.title(),forecast))
    elif city not in weather:
        forecast = random.choice(psblewthr) #kuleki
        history.append((city.title(), forecast)) #gence
        weather[city]=forecast #gence = kuleki
        print(f'{city.title()} ━━━> {forecast}') 


print("Tarixce: ")

for i, (city,forecast) in enumerate(history,start=1):
    print(f'{i}. {city} ━━━> {forecast}')
