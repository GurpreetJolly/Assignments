from openai import OpenAI

with open("./assignment_20260301_sentiment_analysis/openai_api_key", "r") as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)

def get_chatgpt_response(prompt):
    # Define the model and parameters
    model_engine = "gpt-3.5-turbo"  # You can use other models like "text-davinci-003"
    response = client.chat.completions.create(model=model_engine,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])

    # Extract the response text
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    prompt = "What is the capital of France?"
    response = get_chatgpt_response(prompt)
    print("ChatGPT Response:", response)
