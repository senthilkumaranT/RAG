from pydantic import BaseModel
from openai import OpenAI

client =  OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)


class inventory(BaseModel):
    bitcoin : bool
    pepepad : bool
    
    

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Extract the inventory information."},
        {"role": "user", "content": "explain the topic about pepepad"},
    ],
    response_format=inventory,
)

event = completion.choices[0].message.parsed

if event.bitcoin:
    print("bitcoin is true")
else:
    print("bitcoin is false")

if event.pepepad:
    print("pepepad is true")
else:
    print("pepepad is false")
