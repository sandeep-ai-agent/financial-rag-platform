# REAL ENTERPRISE DEAL -  COUNT TOKENS BEFORE CALLING INPUT TOKENS( Cost Estimation ) using tiktoken

import tiktoken


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    encoding = tiktoken.encoding_for_model(model_name=model)
    return len(encoding.encode(text))

prompt_text = "Explain P/E Ratio in complete sentecnt is 2 lines"
print(f"Estimated Inout tokens are : {count_tokens(text=prompt_text)}")


# Build a Cost Calculator both for Input and ouptout toekns

INPUT_COST_PER_1_MILLION = 0.15
OUTPUT_COST_PER_1_MILLION = 0.60

def calculate_cost(prompt_tokens: int , completion_tokens: int) -> float:
    input_cost = (prompt_tokens / 1000000) * INPUT_COST_PER_1_MILLION
    output_cost = (completion_tokens / 1000000) * OUTPUT_COST_PER_1_MILLION
    total_cost = input_cost + output_cost

# This we are gettong from response.usage api from openai api
cost = calculate_cost(response.uasage.prompt_tokens, response.usage.completion_tokens)
print(f"This call cost is ${cost:.6f}")


