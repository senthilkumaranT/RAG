from openai import OpenAI

       #opena i client
client = OpenAI(
  base_url="",#openrouter
  api_key=""#openrouter api key
)

#chat completion
def chat_completion(question):
    for i in client.chat.completions.create(
      model="openai/gpt-4o-mini",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": question
            }
          ]
        }
      ],stream=True
    ):
      print(i.choices[0].delta.content,end="")


 