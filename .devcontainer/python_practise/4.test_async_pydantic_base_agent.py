import pytest 
from pydantic import ValidationError
from pydantic_practice import StockQuote


# Doing testing on already built Code
# 1. Use assert statements – If assertion is False , test fails.
# 2. Pytest.raises() – tests that an error IS raised

def test_stock_quote_valid():
    quote = StockQuote(ticker="AAPL", price=150.5, timestamp="2025-08-19")
    assert quote.ticker == "AAPL"
    assert quote.currency == "USD"   # DEfault value check if not true assert gives false

def test_stock_quote_invalid_price():
    with pytest.raises(ValidationError):
        StockQuote(tocker="AAPL", price="not_a_number", timestamp="2025-09-15")


# and we will build from here on 