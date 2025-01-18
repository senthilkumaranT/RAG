from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)
def get_weather(location):
    return f" {location} "

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                }
            },
            "required": [
                "location"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is the weather like in Paris today?"}],
    tools=tools
)

DN_NAME= completion.choices[0].message.tool_calls[0].function.name

if DN_NAME == "get_weather":
    function_call = completion.choices[0].message.tool_calls[0].function.arguments

print(get_weather(function_call))
