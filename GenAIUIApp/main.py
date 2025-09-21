
import gradio as gr
import config
import utils

chat_history = []
def main():
    def chat_with_memory(user_input,history):
        chat_history.append({"role": "user", "content": user_input})
        response = utils.chat_with_gemini(chat_history)
        chat_history.append({"role": "assistant", "content": response})
        return response

    gr.ChatInterface(fn=chat_with_memory, type="messages").launch()
if __name__ == "__main__":
    main()