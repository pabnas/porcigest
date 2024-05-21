
def snake_case_to_title(snake_case_string, decorator='* '):
    # Split the snake case string into words
    words = snake_case_string.split('_')
    # Capitalize the first word and lowercase the rest, then join them with a space
    title_case_string = ' '.join(words[0].capitalize() if i == 0 else word for i, word in enumerate(words))
    return title_case_string + decorator
