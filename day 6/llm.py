from openai import OpenAI

cli=  OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

#A function
def chat_completion(messages, model):
    response_text = " "
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
            response_text += chunk.choices[0].delta.content

    return response_text