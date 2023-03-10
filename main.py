import requests
import send_email
import datetime
import unidecode

topic = "tesla"

URL = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2022-12-24" \
      "&sortBy=publishedAt&" \
      "apiKey=d81785cd88a748cab6f18bf24d97f219" \
      "&language=en"

API_KEY = "d81785cd88a748cab6f18bf24d97f219"
CURRENT_TIME = datetime.datetime.now().strftime("%A %B %Y")
SUBJECT = f"News for {CURRENT_TIME}"

request = requests.get(url=URL)
content = request.json()

message = ""
number_articles = 20
for article in content["articles"][:number_articles]:
    message = f"{message}\n{article['title']}\n{article['description']}\n{article['url']}\n"

message = unidecode.unidecode(message)
send_email.email_news(message, SUBJECT)
print(type(content))

