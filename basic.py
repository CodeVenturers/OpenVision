import random

# Define a list of predefined responses
responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm just a computer program, so I don't have feelings, but I'm here to assist you!",
    "what's your name": "I'm a simple AI chatbot.",
    "bye": "Goodbye! Have a great day!"
}

# Main function to interact with the AI
def chat_with_ai():
    print("AI: Hello! I'm your friendly chatbot. Ask me anything, or just say 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for case insensitivity

        if user_input == "bye":
            print("AI: Goodbye! Have a great day!")
            break

        response = responses.get(user_input, "AI: I'm sorry, I don't understand that. Please ask something else.")
        print("AI:", response)

if __name__ == "__main__":
    chat_with_ai()
