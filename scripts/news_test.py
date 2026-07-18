import pprint
import yfinance as yf

ticker = yf.Ticker("TCS.NS")

news = ticker.news

print(type(news))
print()

print(f"Total Articles: {len(news)}")
print()

if news:
    pprint.pp(news[0])