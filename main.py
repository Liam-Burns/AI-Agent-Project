import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# locating the API key the calls back to the LLM
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# adds helpful text to user and exits the program if the user does not enter a prompt
if len(sys.argv) == 1:
    print("Please input a prompt")
    exit(1)

#the user's actual prompt text that they submitted
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
    if '--verbose' in sys.argv: # the response to be used if the user includes '--verbose' in their submission
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        #print out the response that comes from the model
        print(response.text)

if __name__ == "__main__":
    main()
