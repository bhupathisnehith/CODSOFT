from datetime import datetime
import random

def chatbot(user_input):
   
    user_input = user_input.lower()

   
    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! How can I help?"])

    elif "how are you" in user_input:
        return random.choice(["I'm just a chatbot, but I'm functioning perfectly! How about you?", "I'm doing great! How can I assist you?", "All systems are working fine! How are you?"])

    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot. You can call me ChatBot!"

    elif "time" in user_input:
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."

    elif "date" in user_input:
        now = datetime.now()
        return f"Today's date is {now.strftime('%Y-%m-%d')}."

    elif "weather" in user_input:
        return "I'm sorry, I can't provide real-time weather information. But I hope it's nice wherever you are!"

    elif "joke" in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts!"
        ]
        return random.choice(jokes)

    elif "thank you" in user_input or "thanks" in user_input:
        return random.choice(["You're welcome! 😊", "No problem! 😄", "Happy to help! 😊"])

    elif "tell me about yourself" in user_input:
        return "I am a simple rule-based chatbot designed to assist you with basic queries. I can tell you the time, date, and even crack a joke!"

    elif "help" in user_input:
        return "Sure! I can help you with the following:\n- Tell you the time\n- Tell you the date\n- Tell you a joke\n- Answer basic questions\n- Play a game\nJust ask!"

    elif "play a game" in user_input or "game" in user_input:
        return "Let's play a number guessing game! Think of a number between 1 and 10, and I'll try to guess it. Ready? Is it 7?"

    elif "yes" in user_input and "game" in user_input:
        return "Yay! I guessed it right! 🎉"

    elif "no" in user_input and "game" in user_input:
        return "Oops! I guess I need to work on my guessing skills. 😅"

    elif "favorite color" in user_input:
        return "I don't have a favorite color, but I like all the colors of the rainbow!"

    elif "favorite food" in user_input:
        return "I don't eat, but if I could, I'd probably love some binary code! �"

    elif "tell me a fact" in user_input or "fact" in user_input:
        facts = [
            "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
            "Bananas are berries, but strawberries aren't.",
            "Octopuses have three hearts."
        ]
        return random.choice(facts)

    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(["Goodbye! Have a great day!", "See you later! 👋", "Bye! Take care!"])

    else:
        return "I'm not sure how to respond to that. Can you ask something else?"


if __name__ == "__main__":
    print("Welcome to the ChatBot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = simple_chatbot(user_input)
        print(f"ChatBot: {response}")
