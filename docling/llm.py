from openai import OpenAI


# openai client
client = OpenAI(
    base_url="",# use your base url
    api_key="",# use your api key
)

# # A function
# def token(messages, model):
#     response_text = " "
#     response = client.chat.completions.create(
#         model=model,
#         messages=[
#             {
#                 "role": "system",
#                 "content": "you are a youtube video expert and you can answer the question based on the video"
#             },
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": messages
#                     },
                  
#                 ]
#             }
#         ],
#         stream=True
#     )

#     for chunk in response:
#         if chunk.choices[0].delta.content:
#             response_text += chunk.choices[0].delta.content

#     return response_text


# chat completion
def chat_completion(messages,model):
    for i in client.chat.completions.create(
      model=model,
      messages=[
            {
                "role": "system",
                "content": "you are a document expert and you can answer the question based on the document"
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
    ):
      print(i.choices[0].delta.content,end="")
