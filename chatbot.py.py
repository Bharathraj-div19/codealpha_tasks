def get_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    elif "your name" in user_input:
        return "I'm a simple chatbot built for the CodeAlpha internship."
    elif "help" in user_input:
        return "You can say hello, ask how I am, or say bye to exit."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Try asking something else."


def run_chatbot():
    print("Chatbot: Hello! Type 'bye' anytime to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    run_chatbot()