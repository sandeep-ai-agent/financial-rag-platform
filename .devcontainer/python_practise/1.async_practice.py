import asyncio
import time

# QUESTION - Write 3 async functions that simulate 3 different "APIs" with different 
# response times (e.g., 2 sec, 3 sec, 1 sec). Use asyncio.sleep() 
# (NOT time.sleep() — that's the common mistake, time.sleep() blocks everything, 
# asyncio.sleep() doesn't). Each should print when it starts and when it finishes.

async def fetch_stock_price():
    print("Fetching Stock Price")
    await asyncio.sleep(2) # It waits for response from API for 2s and does other work parallelly
    print("Stock Price Fetched !")
    return "AAPL: $150"

async def fetch_news_Sentiment():
    print("Fetching News Sentiments")
    await asyncio.sleep(3)  # It waits for response from news API for 3s and does other work parallelly
    print("News Sentiments Fetched")
    return "News Sentiments In India : Very Postive"

async def fetch_risk_score():
    print("Fetching Risk Score")
    await asyncio.sleep(1) 
    print("Risk Score Fetched")
    return "Risk score fetched is : 10"

# Now define main function for it to check for async
async def main_sequential():
    start = time.time()
    stock_price = await fetch_stock_price()
    news_sentiment = await fetch_news_Sentiment()
    risk_score = await fetch_news_Sentiment()
    end = time.time()
    print(f"Sequential Results: {stock_price}, {news_sentiment}, {risk_score}")
    print(f"Sequential time : {end - start:.2f} seconds")

# now define main using asyncio.gather to calculate what father does(all 3 concurrently)

# This took 8 seconds

async def main_parallel():
    start = time.time()
    stock_price, news_sentiment, risk_score = await asyncio.gather(
        fetch_stock_price(),
        fetch_news_Sentiment(),
        fetch_risk_score()
    )
    end = time.time()
    print(f"Parallel Results: {stock_price}, {news_sentiment}, {risk_score}")
    print(f"PArallel Time : {start- end:.2f} seconds")

# this took 3 seconds


if __name__ == "__main__":
    asyncio.run(main_sequential())
    print("***********")
    asyncio.run(main_parallel())

