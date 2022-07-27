import play
import menu
import glob
import os


def welcome():
    print("Welcome to Mad Libs!")


def main_menu():
    main_menu = [
        "View Directions",
        "Play a Game",
        "Create your own Mad Libs",
        "Exit"
    ]
    choice = menu.display_menu(main_menu)
    menu_response(choice)


def menu_response(choice):
    if choice == '1' or choice == '[1]':
        directions = open('mad_libs/directions.txt')
        print(directions.read())
    elif choice == '2' or choice == '[2]':
        display_game_options()
    elif choice == '3' or choice == '[3]':
        create_game()
    elif choice == '4' or choice == '[4]':
        exit()
    else:
        print("Please choose a valid menu option!")
    main_menu()


# Choice 2 - Play a game
def display_game_options():
    options = get_game_options()
    result = menu.display_menu(options, "Which game would you like to play?")
    play.mad_libs(options[int(result)-1] + ".txt")


def get_game_options():
    game_options = []
    os.chdir("mad_libs/games")
    for file in glob.glob("*.txt"):
        game_options.append(file[:len(file)-4])
    return(game_options)


# Choice 3 - Create your own Mad Libs
def create_game():
    print(open("mad_libs/create_game_directions.txt").read())
    options = ["Create your own Mad Libs game from a .txt file",
               "Write your own mad libs game"]
    choice = menu.display_menu(options)

    if choice == '1' or choice == '[1]':
        location = menu.prompt(
            "Please type the location of your Mad libs file")
        play.mad_libs(location)
    elif choice == '2' or choice == '[2]':
        story = menu.prompt(
            "Write your story! Press Enter when you are finished")
        with open("temp.txt", "w") as file:
            file.write(story)
        play.mad_libs("temp.txt")
    else:
        print("Please choose a valid option")
        create_game()


welcome()
main_menu()
