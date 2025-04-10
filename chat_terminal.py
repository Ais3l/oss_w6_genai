import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

chat = genai.GenerativeModel("gemini-1.5-flash").start_chat(history=[])

print("🔹 Gemini Chatbot (종료하려면 'exit' 입력) 🔹")
while True:
    msg = input("You: ")
    if msg.strip().lower() == "exit":
        break
    response = chat.send_message(msg)
    print("Gemini:", response.text)