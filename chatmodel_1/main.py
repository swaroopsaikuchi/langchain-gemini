import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDLUR8Xye5z4zuvBJ_zaQVupmcYbovcgeg"

# Initialize the Gemini 2.0 Flash model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,  
    max_tokens=None,  
    timeout=None,  
    max_retries=2,  
)

# Chat function
def chat_with_bot():
    print("Welcome to the Gemini Chatbot! Type 'exit' to stop the conversation.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        try:
            response = llm.invoke(user_input)  # ✅ Corrected
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Chatbot: An error occurred - {str(e)}")

# Run chatbot
if __name__ == "__main__":
    chat_with_bot()
