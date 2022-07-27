def prompt(prompt_value):
    return input("\n" + prompt_value + ': ')


def display_menu(list, prompt_value="Please choose an option"):
    count = 1
    print("\n")
    for item in list:
        line = "[" + str(count) + "] " + item
        print(line)
        count += 1
    return prompt(prompt_value)
