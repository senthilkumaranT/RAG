from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="",
)

# A function
def token(messages, model):
    response_text = " "
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "you are a youtube video expert and you can answer the question based on the video"
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": messages
                    },
                  
                ]
            }
        ],
        stream=True
    )

    for chunk in response:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content

    return response_text