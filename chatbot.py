import openai

openai.api_key = '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'


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "What is the circumference in km of the planet Earth?"}]
)

reply_content = completion.choices[0].message.content
print(reply_content)