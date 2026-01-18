# name: Jordan Davies
# student_id: 1857892197
import json
import csv
from bs4 import BeautifulSoup

print("reading market card data")
with open("../data/raw_data/web_data.json", "r", encoding="utf-8") as f:
	data = json.load(f)

print("extracting fields from market card data")
cards = data.get("FormattedQuoteResult", {}).get("FormattedQuote", [])

with open("../data/processed_data/market_data.csv", "w", newline="", encoding="utf-8") as f:
	writer = csv.writer(f)

	writer.writerow(["marketCard_symbol", "marketCard_stockPosition", "marketCard_changePct"])

	print("writing market card data to csv")
	for card in cards:
		symbol = card.get("shortName", "")
		stockPosition = card.get("last", "")
		changePct = card.get("change_pct", "")
		writer.writerow([symbol, stockPosition, changePct])
	print("market_data.csv created")

print("reading latest news data")
with open("../data/raw_data/web_data.html", "r", encoding="utf-8") as f:
	html = f.read()

print(type(html))
soup = BeautifulSoup(html, "html.parser")
news_list = soup.find("ul", class_="LatestNews-list")

print("extracting fields from latest news data")
items = news_list.find_all("li", class_="LatestNews-item")

with open("../data/processed_data/news_data.csv", "w", newline="", encoding="utf-8") as f:
	writer = csv.writer(f)

	writer.writerow(["LatestNews_timestamp", "LatestNews_title", "LatestNews_link"])

	print("writing latest news data to csv")
	for item in items:
		timestamp_tag = item.find("time", class_="LatestNews-timestamp")
		timestamp = timestamp_tag.get_text(strip=True)

		a_tag = item.find("a", class_="LatestNews-headline")
		title = a_tag.get("title", "").strip()
		link = a_tag.get("href", "").strip()

		writer.writerow([timestamp, title, link])
	print("news_data.csv created")
