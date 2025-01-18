from openai import OpenAI

client = OpenAI(
    base_url="",
    api_key="",
)

# A function
def token(messages, model, url):
    response_text = " "
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a brain tumor expert and you can answer the question based on the image"
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": messages
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": url
                        }
                    }
                ]
            }
        ],
        stream=True
    )

    for chunk in response:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content

    return response_text