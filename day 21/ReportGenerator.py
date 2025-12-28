import requests
import datetime

class ReportGenerator:
    def BitcoinPrice(self):
        url = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
        data = url.json()
        return data["data"]["rates"]["USD"]
    
    def RandomQuote(self):
        url = requests.get("https://api.kanye.rest")
        data = url.json()
        return data["quote"]

Bitcoin1 = ReportGenerator()
Quotes = ReportGenerator()
mixeddate = datetime.datetime.now()
date = mixeddate.strftime("%y/%m/%d")

with open("report.txt", "a") as file:
    file.write(f"--Report {date}-- \n BTC Price: {Bitcoin1.BitcoinPrice()} \nQuote of the Day: {Quotes.RandomQuote()} \n\n")
    print("Reported Successfully")