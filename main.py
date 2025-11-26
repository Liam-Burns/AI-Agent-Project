
#importing the API text from our .env file
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

#importing the API Key for Gemini LLM
from google import genai

client = genai.client(api_key=api_key)


#main function to run
def main():
    print("Hello from ai-agent-project!")


if __name__ == "__main__":
    main()
