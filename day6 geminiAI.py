from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key1=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key1)
while True:
    question=input("you: ")
    if question.lower()=="exit":
        break
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    print("Gemini:",response.text)