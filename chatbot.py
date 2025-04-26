import gradio as gr

def simple_chatbot(message):
    message_lower = message.lower()

    if any(greet in message_lower for greet in ["hello", "hi", "hey"]):
        reply = "Hello! 👋 How can I help you today?"
    elif "how are you" in message_lower:
        reply = "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in message_lower:
        reply = "I'm your friendly chatbot! You can call me ChatSimple 🤖"
    elif "weather" in message_lower:
        reply = "I'm not connected to real weather data yet, but I hope it's sunny where you are! ☀️"
    elif "hobby" in message_lower or "what do you do" in message_lower:
        reply = "I enjoy chatting with you! 🤖"
    elif "bye" in message_lower or "goodbye" in message_lower:
        reply = "Goodbye! Have a wonderful day! 👋"
    elif "help" in message_lower:
        reply = "I'm here to chat! Try asking me about my name, hobbies, or just say hello!"
    else:
        reply = "Hmm... I don't have an answer for that yet. But I'm learning every day! 😊"

    return reply

# Gradio Interface
demo = gr.Interface(
    fn=simple_chatbot,
    inputs=gr.Textbox(label="Your Message"),
    outputs=gr.Textbox(label="Chatbot Reply"),
    title=" Simple Chatbot ",
    description="Chat with me and ask me about my hobby🥧🤖"
)

demo.launch(share=True, server_name ='0.0.0.0') # listen to all interfaces
