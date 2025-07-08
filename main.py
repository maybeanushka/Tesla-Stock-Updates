from dotenv import load_dotenv
load_dotenv()
import os
import requests
from smtplib import SMTP
from email.message import EmailMessage
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
sender = "anushkapchaudhari90@gmail.com"
password = os.environ.get("PASSWORD")
receiver = "anushkapchaudhari9@gmail.com"

PARAMETERS= {"function":"TIME_SERIES_DAILY",
             "symbol":STOCK,
             "apikey":STOCK_API_KEY}
try:
    response = requests.get(url='https://www.alphavantage.co/query', params= PARAMETERS)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching stock data: {e}")
else:
    data = response.json()["Time Series (Daily)"]
    dates = list(data.keys())
    today_data = float(data[dates[0]]['4. close'])
    yesterday_data = float(data[dates[1]]['4. close'])
    dby_data = float(data[dates[2]]['4. close'])

    diff = (yesterday_data - dby_data) / dby_data
    if diff > 0:
        symbol = "🔺"
    else:
        symbol = "🔻"
    percentage = abs(diff)*100

    news_parameters={'apiKey': NEWS_API_KEY,
                     'q': COMPANY_NAME,
                     "language":"en"}
    news = requests.get(url="https://newsapi.org/v2/everything", params= news_parameters)
    news_data = news.json()["articles"][:3]
    formatted_articles = [(f"\nHeadline: {article['title']}.\n"
                           f"Brief: {article['description']}\n") for article in news_data]

    message = f"{STOCK}: {symbol}{round(percentage,1)}%\n"
    message += "\n".join(formatted_articles)


    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = f"{STOCK} Stock Alert: {symbol}{round(percentage, 1)}%"
    msg.set_content(message)

    with SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(user= sender, password= password)
        server.send_message(msg)
    print("Message sent successfully!")
