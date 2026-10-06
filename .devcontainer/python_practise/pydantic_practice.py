from pydantic import BaseModel, Field
from typing import Optional

# Defining pydantic class inherting from BAseModel

# this is old way with pydantic we will use Field
# class StockQuote(BaseModel):
#    ticker: str
#   price: float
#   currency: str = "USD"
#   timestamp: str 

# Create class using Field

class StockQuote(BaseModel):
    ticker: str
    price: float = Field(description="Field must be positive")
    currency: str = "USD"
    timestamp: str = Field(description = "This field must be str type only")


# instantiate this class and do the test validation 

stock = StockQuote(ticker="AAP", price= -150.25, timestamp="2026-09-15")
print(stock)

print("\n*********\n")
# Convert it to Python Dictionary
print(stock.model_dump())


# Now break it on purpose and see what happens

#2c. wrong_stock = StockQuote(ticker="AAP", price = "two hundered rupees", timestamp = "2025-10-15")
#print(wrong_stock)


# 2e.The real-world one — nested models (this is what you'll actually use in RAG). Build a DocumentChunk model like this:

# Try instantiating a DocumentChunk with nested ChunkMetadata 

class ChunkMetaData(BaseModel):
    source_filter: str
    page_number: int
    company: str


class DocumentChunk(BaseModel):
    chunk_id: str
    text: str
    metadata: ChunkMetaData
    embedding: Optional[list[float]] = None


