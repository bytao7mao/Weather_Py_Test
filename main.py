import requests


def main():
    city = input("Enter City:")
    city_already_inputed = 'tokyo'
    api_key = "48ebea5a0b5c48637b05be3e27ea0d91"
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, api_key)
    url2 = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    res = requests.get(url2)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']

    print('Temperature:', temp, '°C')
    print('Wind:', wind)
    print('Pressure: ', pressure)
    print('Humidity: ', humidity)
    print('Description:', description)


if __name__ == "__main__":
    main()
