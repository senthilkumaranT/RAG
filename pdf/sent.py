from openai import OpenAI

       #openai client
client = OpenAI(
  base_url="",
  api_key=""
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

