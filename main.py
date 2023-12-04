import openai

openai.api_key = "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"

def chat_with_gpt(promt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role" : "user" , "content" : promt}]
    )

    return response['choices'][0]['message']['content'].strip()



if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit" , "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot" , response)
