from openai import OpenAI

cli= OpenAI(
    base_url="",
    api_key="",
)

def chat_completion(messages, model):
    response = cli.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "you are document expert and answer the question based on the document " 
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
            yield chunk.choices[0].delta.content