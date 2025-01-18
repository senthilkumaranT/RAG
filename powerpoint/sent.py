from openai import OpenAI
import streamlit as st

#openai client
client = OpenAI(
  base_url="",
  api_key="",

)

#chat completion
def chat_completion(question):

    response_text = ""
    response = client.chat.completions.create(
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
      ],
      stream=True
    )
    for chunk in response:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content
          
    return response_text
      

