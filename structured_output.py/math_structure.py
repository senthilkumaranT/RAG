from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
     base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
        {"role": "user", "content": "how can I solve 8x + 7 = -23"}
    ],
    response_format=MathReasoning,
)

math_reasoning = completion.choices[0].message.parsed



print(math_reasoning)