from openai import OpenAI  # Import the OpenAI library to interact with the OpenAI API

# Initialize the OpenAI client with base URL and API key
cli = OpenAI(
    base_url="",  # Base URL for the OpenAI API
    api_key="",   # API key for authentication
)

def chat_completion(messages, model):
    # Create a chat completion request to the OpenAI API
    response = cli.chat.completions.create(
        model=model,  # Specify the model to use for the completion
        messages=[  # Define the messages for the chat
            {
                "role": "system",  # System message to set the context
                "content": "You are a cooking expert. The user will provide the ingredients they have, and you will suggest a recipe using those ingredients."
            },
            {
                "role": "user",  # User message containing the input
                "content": messages  # The user's input message
            }
        ]
    )
    
    # Extract the content of the response message
    message_content = response.choices[0].message.content
    
    return message_content  # Return the content of the response