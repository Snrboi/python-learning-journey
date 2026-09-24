def process_prompt(prompt):

    # Create a nested function called clean_prompt
    # It should strip whitespace and convert the text to lowercase.

    # Call clean_prompt using prompt

    # Return the cleaned result
    def clean_prompt(prompt):
        cleaned = prompt.strip().lower()
        return cleaned
    cleaned_prompt = clean_prompt(prompt)
    return cleaned_prompt

result = process_prompt("   BUILD ME AN AI APP   ")
print(result)