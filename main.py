import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) == 1:
    print("Please input a prompt")
    exit(1)

user_prompt = sys.argv[1]

# create messages after we have the prompt
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

def main():
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
    )

    print("Hello from ai-agent-project!")
    #print out the response that comes from the model
    print(response.text)
    #prints out tokens used during response
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
