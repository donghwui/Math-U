import openai
import prompt_formatter as pf

# API Key (pls don't show anyone, money is attached to this)
openai.api_key = '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'

# boolean for determining when to stop
end = False

# handles the opening message
def opening():
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
    return initial_prompt + "\n" + response


# handles asking user for their question and outputting response
def ask_and_response(chat_history_text):
    # asks user to enter their question
    question = input("Please Enter Your Question: ")

    # checks to end program
    if question == "end":
        end = True
        return "Chat ended"

    prompt = pf.prompt_with_history(chat_history_text, question)


    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": question}]
    )

    response = completion.choices[0].message.content
    print(response)
    return question + "\n" + response


with open("chat_history.txt", 'r+') as chat_history:
    chat_history.write(opening())
    while not end:
        chat_history_text = chat_history.read()
        chat_history.write(ask_and_response(chat_history_text))






