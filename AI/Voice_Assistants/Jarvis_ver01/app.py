# conda activate jarvis
# чат с llama3-70b-8192 через API groq

from groq import Groq

groq_client = Groq(api_key="YOUR KEY")

def  groq_prompt(prompt):
    convo = [{'role': "user", 'content': promt}]
    chat_completion = groq_client.chat.completions.create(messages=convo, model='llama3-70b-8192')
    response = chat_completion.choices[0].message

    return response.content

prompt = input('USER:')
response = groq_prompt(prompt)
print(response)