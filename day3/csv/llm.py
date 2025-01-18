from openai import OpenAI 

client = OpenAI(
  base_url="",
  api_key="",
)

# def token(messages,model):  
#     for token in client.chat.completions.create(
#      model=model,
#         messages=[
#         {
#         "role": "user",
#         "content": [
#             {
#             "type": "text",
#             "text": messages
            
#             } 
            
#         ]
#         }
#     ],
#     stream=True
    

#     ):
#          print(token.choices[0].delta.content,end='')


#chat completion
def chat_completion(question,model):

    response_text = ""
    response = client.chat.completions.create(
      model=model,
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
      ],
      stream=True
    )
    for chunk in response:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content
          
    return response_text
      