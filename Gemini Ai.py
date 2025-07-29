import google.generativeai as genai

# Set your API key
genai.configure(api_key="                                                   ")  # Replace with your actual API key

# Initialize a conversation history
conversation_history = []

def generate_response(prompt):
    # Build the full conversation context
    context = "\n".join(conversation_history) + f"\nUser: {prompt}"

    # Set up the model
    model = genai.GenerativeModel("gemini-1.5-flash")  # Using the gemini model

    # Generate the response using generate_content
    response = model.generate_content(context)

    # Add user prompt and AI response to the history
    ai_response = response.text
    conversation_history.append(f"User: {prompt}")
    conversation_history.append(f"AI: {ai_response}")

    return ai_response

# Main loop for multi-prompt interaction
print("Start a conversation with the AI! Type 'exit' to end.\n")

while True:
    user_prompt = input("You: ")
    if user_prompt.lower() == "exit":
        print("Goodbye!")
        break

    response = generate_response(user_prompt)
    print(f"AI: {response}")
