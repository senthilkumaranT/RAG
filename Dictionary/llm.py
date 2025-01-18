from openai import OpenAI



client = OpenAI(
    url="",
    api_key="",
)


def chat_completion(question):
    for i in client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":[
                    {
                        "type":"text",
                        "text":question
                    }
                ]
            }
        ]
    )

