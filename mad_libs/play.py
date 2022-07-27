import menu


def mad_libs(file):
    print("Enter values according to the prompts below. Your story will be displayed when you have completed all the prompts.\n")
    file = open(file).read()
    # while there are still prompts
    while(file.find('[') != -1):
        begin = file.find('[')
        # find closing bracket after the current "["
        end = file[begin:].find("]") + begin
        full_prompt = file[begin:end+1]
        prompt_value = file[begin+1:end]
        # replace the prompt with the user's input
        file = file.replace(full_prompt, menu.prompt(prompt_value), 1)
    print("\nAll done! Here is your result: \n" + file)
