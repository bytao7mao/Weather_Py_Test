import smtplib, ssl

import requests
import socket
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# CONSTANTS
API_KEY = '48ebea5a0b5c48637b05be3e27ea0d91'
EMAIL_ADDRESS = 'marius.tao@gmail.com'
EMAIL_PASSWORD = 'Blader888_steelseries'
RECIPIENT_EMAIL = 'marius.a.nicolae@outlook.com'
LOCATION = 'BUCHAREST'
PORT = 465

gmailAppPassword = 'iall iibf afeg jrkr'


# def fetch_weather(api_key, location):
#     base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
#     response = requests.get(base_url)
#     return response.json()
#
#
# def compose_email(weather_data):
#     weather = weather_data['weather'][0]['main']
#     temp = weather_data['main']['temp']
#     advice = "It's a warm day, consider wearing light clothes." if temp > 20 else "It might be chilly, consider wearing a jacket."
#     message = f"Good morning! Today's weather in {LOCATION}: {weather}, {temp}°C. {advice}"
#     return message
#
#
def send_email(city, degrees):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Weather news from tao !"
    message["From"] = EMAIL_ADDRESS
    message["To"] = RECIPIENT_EMAIL

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Marius Nicolae has great Linkedin Profile:
    https://www.linkedin.com/in/nicolae-marius-37b344144/"""
    html = f"""\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="https://www.linkedin.com/in/nicolae-marius-37b344144/">Linkedin Profile</a> 
           has great profile.
        </p>
        <p>Hi,<br>
           In {city} The Weather is: {degrees} '°C'
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    # part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    # message.attach(part1)
    message.attach(part2)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login(EMAIL_ADDRESS, gmailAppPassword)
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, message.as_string())

    print("Email sent!")


def main():
    # var = socket.getaddrinfo('localhost', 8080)
    # print(var)
    # weather_data = fetch_weather(API_KEY, LOCATION)
    # email_body = compose_email(weather_data)
    # send_email("Today's Weather Alert", email_body)

    # city = input("Enter City:")
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, api_key)
    url2 = f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric"

    res = requests.get(url2)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    # temp: int = data['main']['temp']
    temp = int(data['main']['temp'])

    print('Temperature:', temp, '°C')
    print('Wind:', wind)
    print('Pressure: ', pressure)
    print('Humidity: ', humidity)
    print('Description:', description)

    body = 'Temperature:  ' + str(temp)
    subject = "Weather news!"

    send_email(LOCATION, temp)


if __name__ == "__main__":
    main()
