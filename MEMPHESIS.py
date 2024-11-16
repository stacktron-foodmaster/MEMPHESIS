import re
import time
import sys

# Memory to store user information
memory = {}


def print_animation():
    frames = [
        "    O\n   /|\\\n   / \\\n   ⚽",
        "    O\n   /|\\\n   / \\\n    ⚽",
        "    O\n   /|\\\n   / \\\n     ⚽",
        "    O\n   /|\\\n   / \\\n      ⚽",
    ]
    for frame in frames:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.3)  # Adjust speed as needed
    print()  # Newline after animation


def clean_input(user_input):
    corrections = {
        "whats": "what is", "helo": "hello", "thnk": "thank",
        "tnks": "thanks", "gime": "give me", "pleas": "please"
    }
    words = user_input.lower().split()
    corrected_words = [corrections.get(word, word) for word in words]
    return " ".join(corrected_words)


def chatbot_response(user_input):
    user_input = clean_input(user_input)

    try:
        # Check for math operations
        if re.search(r'\d+\s*[+*/-]\s*\d+', user_input):
            try:
                result = eval(user_input)
                return f"The result is {result}"
            except (SyntaxError, NameError):
                return "Sorry, I don't understand that math expression."

        # Memory functionality: Storing user's name
        if "my name is" in user_input:
            name = user_input.split("my name is")[-1].strip()
            memory['user_name'] = name
            return f"Nice to meet you, {name}!"

        if "what is my name" in user_input:
            if 'user_name' in memory:
                return f"Your name is {memory['user_name']}, right?"
            else:
                return "I don't know your name yet. You can tell me by saying 'My name is ...'."

        # Predefined responses using pattern matching
        responses = {
            r"hello": "Hi there! How can I help you today?",
            r"how are you": "I'm just a program, but I'm here to assist you!",
            r"what is your name": ("I'm MEMPHESIS created to help you with your queries, "
                                   "developed by esseg, and some code originated by copilot."),
            r"bye": "Goodbye! Have a great day!",
            r"fact": "I'm a bot built by a 19-year-old who is learning Python and has contributed a lot to Python in the past decade.",
            r"what lan were you built on": "I was built using Python.",
            r"where is the 19-year-old learning": "Cambridge, in England.",
            r"what is minecraft": "It is a 3D sandbox game owned by Microsoft, created by Markus Persson (Notch).",
            r"are you like a buddy": "Yes, I'm like your 'buddy,' but I'm different because I'm AI!",
            r"what in the world is python": "Python is a free programming language made by Guido van Rossum.",
            r"what editor were you made on": "I was built using PyCharm.",
            r"give me a link to youtube": "Sure, here it is: https://youtube.com/",
            r"thank you": "No problem! You deserve a thank you for supporting me 😁😊!",
            r"what is the company that owns you": "I don't have a company, but I will once I am sold 😁!",
            r"how old are you": "I'm a month old.",
            r"where can i buy you": "Contact me at 0911639458.",
            r"are you a built-in project": "No, I was built offline using an editor.",
            r"help me make you": "I recommend using Copilot to help you with my code or opening me in PyCharm.",
            r"i need help by python": "Try this: `print('your name')` or ask Copilot!",
            r"my not in school brother needs help with 1 + 1": "1 + 1 = 2.",
            r"are you smart": "I'm only as smart as the knowledge I have, but you're the real smart one!",
            r"say hi": "Hi!",
            r"give me a link to gmail": "Sure, here it is: https://accounts.google.com/",
            r"give me a link to mendeley": "Sure, here it is: https://www.mendeley.com/",
            r"what is the meaning of stem": "STEM stands for Science, Technology, Engineering, and Mathematics.",
            r"say hello user": f"Hello, {memory.get('user_name', 'user')}!",
            r"thanks": "You're welcome!",
            r"tell me a joke": (
                "Here's a joke: A man went to the doctor. The doctor said, 'I have bad news and worse news.' "
                "The man asked, 'What’s the bad news?' The doctor replied, 'You have 24 hours to live.' "
                "'And the worse news?' The doctor said, 'I forgot to tell you 23 hours ago!' 😂"),
            r"are you loyal": "Yes, I'm loyal to my developer and to you!",
            r"become my friend": "I’m already your friend 😊!",
            r"tell me the name of your developer": "I was developed by Dawit Jr. 😊.",
            r"neural network": "A neural network is a study of AI, like ChatGPT, which uses neural networks.",
            r"i like you": f"thanks, {memory.get('user_name', 'user')}!",
            "how to make a model of you":"download me on github"
        }

        # Check for matching patterns in user input
        for pattern, response in responses.items():
            if re.search(pattern, user_input):
                return response

        return "I'm sorry, I don't understand that. Please try again. 🙏"

    except TypeError:
        return "Sorry, I don't understand that. Please check the input type."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def main():
    print("             MEMPHESIS AI")
    print(
        "New update coming soon in the Minecraft movie release! Want to help for free or be the co-founder? Join me on Discord!")
    print()
    print("MEMPHESIS: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("Enter your question or chat with MEMPHESIS: ")
        if user_input.lower() == "bye":
            print_animation()  # Play animation before exiting
            print("MEMPHESIS: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print_animation()  # Show animation first
        print(f"MEMPHESIS: {response}")  # Print the response after animation


if __name__ == "__main__":
    main()
