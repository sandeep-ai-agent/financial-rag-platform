import os
from dotenv import load_dotenv
from openai import OpenAI 
import tiktoken

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "system", "content": "You are a financial analysi assitant"},
        {"role": "user", "content": "Explain what is P/E ratio in 2 sentences"}
    ]
)

print(response.choices[0].message.content)


# Inspect the FULL Response Object instead of just the text.

print("******   COMPLETE LOGS *********")
print(response.usage)


# REAL ENTERPRISE DEAL -  COUNT TOKENS BEFORE CALLING ( Cost Estimation ) using tiktoken

INPUT_COST_PER_1_MILLION = 0.15  # This is current gpt-40-mini pricing
OUTPUT_COST_PER_1_MILLION = 0.60  # # This is current gpt-40-mini pricing

def calculate_cost(prompt_tokens: int , completion_tokens: int) -> float:
    input_cost = (prompt_tokens / 1000000) * INPUT_COST_PER_1_MILLION
    output_cost = (completion_tokens / 1000000) * OUTPUT_COST_PER_1_MILLION
    return input_cost + output_cost

# This we are gettong from response.usage api from openai api
cost = calculate_cost(response.usage.prompt_tokens, response.usage.completion_tokens)
print(f"This call cost is ${cost:.6f}")