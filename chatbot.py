import openai
import prompt_formatter as pf

# API Key (pls don't show anyone, money is attached to this)
openai.api_key = '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'

# asks user to choose a major
major = input("Enter Major You're Interested In: ")

# gets initial prompt
initial_prompt = pf.get_prompt(major)

# opening message
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": initial_prompt}]
)

response = completion.choices[0].message.content
print(response)