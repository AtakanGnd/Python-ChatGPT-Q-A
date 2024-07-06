from openai import OpenAI

client = OpenAI(
  api_key="API-KEY",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an AI assistant that provides accurate and detailed answers to any questions asked by the user, ensuring clarity and comprehensiveness."},
    {"role": "user", "content": "Albert Einstein kimdir?"}
  ],
    temperature=0.7,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(completion.choices[0].message)
