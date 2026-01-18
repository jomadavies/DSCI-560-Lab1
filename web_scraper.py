# name: Jordan Davies
# student_id: 1857892197
import requests
import json
from bs4 import BeautifulSoup

# request headers
headers = {
	"User-Agent": "Mozilla/5.0",
	"Accept": "text/html",
	"Accept-Language": "en-us,en;q=0.9"
}

# making the request
response = requests.get("https://www.cnbc.com/world/?region=world", headers=headers)

# parsing the HTML
soup = BeautifulSoup(response.text, "html.parser")

# saving the HTML file
with open("../data/raw_data/web_data.html", "w", encoding="utf-8") as f:
	f.write(soup.prettify())

# get json data for market header
data = requests.get("https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=.STOXX|.GDAXI|.FTSE|.FCHI|.FTMIB&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json&events=1", headers=headers).json()

with open("../data/raw_data/web_data.json", "w", encoding="utf-8") as f:
	json.dump(data, f, ensure_ascii=False, indent=2)

