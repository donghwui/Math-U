# prompt formatter
# a module for chatbot.py

def get_prompt(major):
    prompt = ""

    with open(f"./majors_data/{major}.txt", 'r') as data:
        first_line = data.readline()

        # first part of prompt ----
        prompt += (f"chatgpt, you are now an academic advisor with the purpose of answering any questions given by a student\nYou have this knowledge: \nThe course requirements for a {major} major are:\n")
        prompt += ("--------------------------------------------")


        # context for prompt ----

        # checks if we need to include pre-requirements from table 2
        if "! include table 2" in first_line:
            with open("./majors_data/table2.txt", 'r') as table2:
                table2_contents = table2.read()
                prompt += (table2_contents)

        file_contents = data.read()
        prompt += (file_contents)


        # end of prompt ----
        prompt += ("--------------------------------------------\n")
        prompt += ("Your answers will be based only on the context provided above with no other prior information. All you answers should be formatted as if you were talking to a student directly. Do not mention anything about having the context given above. Please start by asking the student if they have any questions")
    return prompt

