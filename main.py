# import openai library
import openai

# Replace with your API key
API_KEY = "Your_API_Key"

# OpenAI client configuration
openai.api_key = API_KEY

# Conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant and converse naturally."}
]

def chatbot():
    print("Chatbot Started! Type 'exit' to close.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chat closed. Until later!")
            break

        # Adds user input to history
        conversation_history.append({"role": "user", "content": user_input})

        # Calls the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )

        # Gets the wizard's response
        assistant_response = response["choices"][0]["message"]["content"]
        print(f"Chatbot: {assistant_response}\n")

        # Added reply to history
        conversation_history.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    chatbot()
