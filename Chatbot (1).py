import random

responses = {
    "hello": ["Hi there! How can I help you?"],
    "hi": ["Hi there! How can I help you?"],
    "how are you": ["I'm just a chatbot, but I'm doing great! Thanks for asking."],
    "what is your name": ["I'm a simple chatbot created for demonstration purposes."],
    "bye": ["Goodbye! Have a great day!"]
}

default_response = ["I'm sorry, I didn't understand that. Can you please rephrase?"]

def chatbot():
    print("Hello! I'm a simple chatbot. How can I assist you today?")


    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        found = False

        for key in responses:
            if key in user_input:
                print("Chatbot:" + random.choice(responses[key]))
                found = True
                break

        if not found:
            print("Chatbot: " + random.choice(default_response))

chatbot()