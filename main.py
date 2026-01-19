import os
import smtplib
import ssl
import logging
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_env_variable(var_name, default=None, required=True):
    value = os.environ.get(var_name, default)
    if required and not value:
        raise ValueError(f"Environment variable {var_name} is required but not set.")
    return value

def fetch_weather(api_key, location):
    """
    Fetch weather data from OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        return None

def compose_email_parts(weather_data, location):
    """
    Compose plain text and HTML email parts from weather data.
    """
    if not weather_data:
        return None, None

    city = weather_data.get('name', location)
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    text = f"""\
    Hi,
    In {city} the weather is: {temp} °C
    Description: {description}
    """

    html = f"""\
    <html>
      <body>
        <p>Hi,<br>
           In {city} the weather is: {temp} °C<br>
           Description: {description}
        </p>
      </body>
    </html>
    """
    return text, html

def send_email(subject, text_content, html_content, email_address, app_password, recipient_email):
    """
    Send an email using Gmail SMTP.
    """
    if not html_content and not text_content:
        logging.warning("No content to send.")
        return

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = email_address
    message["To"] = recipient_email

    # Attach plain text and HTML parts
    if text_content:
        part1 = MIMEText(text_content, "plain")
        message.attach(part1)
    if html_content:
        part2 = MIMEText(html_content, "html")
        message.attach(part2)

    context = ssl.create_default_context()
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(email_address, app_password)
            server.sendmail(email_address, recipient_email, message.as_string())
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def main():
    try:
        api_key = get_env_variable("WEATHER_API_KEY")
        email_address = get_env_variable("GMAIL_USERNAME")
        gmail_app_password = get_env_variable("gmailAppPassword")
        recipient_email = get_env_variable("RECIPIENT_EMAIL", 'marius.a.nicolae@outlook.com', required=False)
        location = get_env_variable("WEATHER_LOCATION", 'BUCHAREST', required=False)
    except ValueError as e:
        logging.error(e)
        return

    logging.info(f"Fetching weather for {location}...")
    weather_data = fetch_weather(api_key, location)

    if weather_data:
        # Log weather details
        try:
            temp = weather_data['main']['temp']
            wind = weather_data['wind']['speed']
            pressure = weather_data['main']['pressure']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']

            logging.info(f"Temperature: {temp} °C")
            logging.info(f"Wind: {wind}")
            logging.info(f"Pressure: {pressure}")
            logging.info(f"Humidity: {humidity}")
            logging.info(f"Description: {description}")
        except KeyError as e:
            logging.warning(f"Missing data in weather response: {e}")

        text_body, html_body = compose_email_parts(weather_data, location)
        send_email("Weather news from tao!", text_body, html_body, email_address, gmail_app_password, recipient_email)
    else:
        logging.error("Could not fetch weather data. Aborting.")

if __name__ == "__main__":
    main()
