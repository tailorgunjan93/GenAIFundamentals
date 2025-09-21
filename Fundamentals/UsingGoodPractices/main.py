#Generate Code with Good Practices
import utils

def Main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break
        response=utils.chat_with_gemini(user_input)
        utils.log_conversation(user_input, "Gemini: " + response)

    
if __name__ == "__main__":
    Main()  