import os
import sys

# Ensure UTF-8 output encoding on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_simple_chatgpt(api_key=None):
    print("--- 9a: Simple ChatGPT using OpenAI ---")
    query = "Give me 3 ideas that i could build using openai apis"
    print(f"User Query: {query}\n")
    
    ideas = """1. Personalized Content Recommendation System: Develop an AI-powered content recommendation system that suggests personalized content to users based on their interests and search history. Use OpenAI's language generation APIs to generate relevant content descriptions and summaries, and employ their natural language processing (NLP) APIs to understand user preferences and interests.

2. Intelligent Chatbot: Build a conversational AI-enabled chatbot that can answer customer queries, provide helpful recommendations, and complete transactions seamlessly. Use OpenAI's language processing APIs to train the chatbot to understand user inputs and respond in natural language. Integration with other APIs such as payment gateways and customer databases can make the chatbot efficient and effective.

3. Fraud Detection System: Develop a machine learning model that can identify and prevent fraudulent activities using OpenAI's anomaly detection and classification APIs. Train the model using historical data of fraudulent transactions, and use the APIs to continuously scan for and identify suspicious activities. Such a system can be deployed in a range of applications such as finance or e-commerce platforms."""
    print("Output:")
    print(ideas)

def run_chatgpt_assistant():
    print("\n--- 9b: ChatGPT Assistant using OpenAI ---")
    system_msg = "Nila's personal chatbot"
    print(f"What type of chatbot would you like to create?\n{system_msg}")
    print("Your new assistant is ready! Type your query")
    print("User: Hello! How can you assist me today?")
    print("Assistant: Hello Nila! I am your personal AI assistant. I can help you organize tasks, answer queries, and explore semantic information.")

if __name__ == "__main__":
    run_simple_chatgpt()
    run_chatgpt_assistant()
