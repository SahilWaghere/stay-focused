import requests

def read_text_from_file():
    """Reads text from 'adhd.txt' in the current directory."""
    with open('adhd.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def ask_question(api_url, headers, conversation_history, question):
    """Sends a question to the text generation API and returns the answer."""
    payload = {
        "conversation_history": conversation_history,
        "preserve_history": True,
        "question": question,
        "randomness": 0.5,
        "response_type": "text",
        "stream_data": False
        # Removed the training_data line for simplicity and relevance
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def get_chatbot_response(user_message):
    api_url = "https://api.worqhat.com/api/ai/content/v3"
    token = "sk-e253f93ee90e491d870f2e2f7a9e80c9"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Read text from 'adhd.txt' file
    text = read_text_from_file()
    # Convert the extracted text to conversation history format
    conversation_history = [{"Document Content": text}]
    
    # Call ask_question with all required parameters
    response = ask_question(api_url, headers, conversation_history, user_message)
    
    # Process and return the response content
    return response.get("content", "Sorry, I couldn't process your request.")

def main():
    print("Chatbot is ready. Ask me anything about the document.")
    while True:
        question = input("You: ")       
        response = get_chatbot_response(question)
        print("Chatbot:", response)

if __name__ == "_main_":
    main()