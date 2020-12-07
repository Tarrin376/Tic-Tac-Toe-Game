import re
import logging
import time
import copy
import secrets

# Setting up logging for when the user creates a username.

logger = logging.getLogger(__name__)

formatter = logging.Formatter(
    "%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler('Tic Toe Info.log')  # --> File handler
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# ---------------------------------------------------------------------------
# Start of Create Account --> Code that runs if users wants to create account.
# ---------------------------------------------------------------------------


class Account:

    def __init__(self, play=None, name=None):
        self.play = play
        self._name = name

    # --> User chooses name
    def _user_name(self):
        while True:
            self._name = input("Create a username: ")
            regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
            if(regex.search(self._name) == None):
                print("\nUsername is valid\nFinished Setup...\n")
                logger.setLevel(logging.INFO)  # --> Valid
                logger.info(f"Valid username: {self._name}")
                return
            else:
                print("\nUsername cannot contain any special characters.\n")
                logger.setLevel(logging.DEBUG)  # --> Invalid
                logger.debug(f"Invalid username: {self._name}")

    # --> Asks if user wants to play the game
    def user_play(self):
        try:
            self.play = input("Would you like to play as Guest?: ").lower()
        except Exception as ex:
            print(f"Invalid Input {ex} Please Try Again!")
        if self.play == "yes":
            print("\nYou have chosen to play as Guest...\n")
        elif self.play == "no":
            print("\nYou have chosen to setup an account...\n")
            account._user_name()
        else:
            print("Invalid input...")
            account.user_play()


# --> Calling the user_play method in the Class -- Account.
account = Account()
account.user_play()

# ----------------------------------------------------------------------------------------
# Start of Game --> Asks the user if they have already completed the setup for Tic Tac Toe.
# ----------------------------------------------------------------------------------------
grid = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]


class Game:

    print("\n-------------- Welcome to the Tic Tac Toe game --------------\n")

    # --> Attributes for our game.
    def __init__(self, choice=None, number=None, layout=None, numbers_chosen=None, valid_coord=None):
        self.choice = choice
        self.number = number
        self.layout = layout
        self.numbers_chosen = numbers_chosen
        self.valid_coord = valid_coord

        self.numbers_chosen = list()

    def user_choice(self):
        self.choice = input("\nNoughts(o) or Crosses(x)?: ").lower()  # --> Us
        if self.choice == "x" or self.choice == "o":
            print(f"\nYou have chosen {self.choice}!\n")
        else:
            print("Enter either 'x' or 'o'.")
            game.user_choice()

    # -------------------------------------------
    # -- > Calculations for the Tic Tac Toe game.
    # -------------------------------------------

    def grid_board(self):

        # --> Takes coordinate input.
        def coordinates():
            self.number = int(input("Enter number 0-8: "))
            try:
                int(self.number)
            except ValueError as err:  # --> Throws an exception.
                print(f"\nERROR! {err} Please try again!\n")
                coordinates()
            if self.number > 8 or self.number < 0:
                print("Invalid number!")
                coordinates()
            else:
                if "-" in grid:
                    for i in range(len(grid)):  # --> Checks coordinate.
                        if i == self.number:
                            if i not in self.numbers_chosen:
                                grid[i] = self.choice
                                self.numbers_chosen.append(i)
                                break
                            else:
                                print("Coordinate as already been used")
                                coordinates()  # --> If invalid.
        coordinates()

        # --> Prompts the user to ask if they would like to play again (function is ignored until end of game)
        def play_again():
            global grid
            question = input("Would you like to play again?: ")
            if question == "yes".lower() or question == "ok".lower():
                grid = [
                    "-", "-", "-",
                    "-", "-", "-",
                    "-", "-", "-"
                ]
                self.numbers_chosen = []
                self.valid_coord = []
                game.user_choice()
            elif question == "no".lower():
                print("\n------------------")
                print("Exiting Program...")
                print("------------------")
                time.sleep(3)
                exit()
            else:
                print("\nPlease answer 'yes' or 'no'\n")
                play_again()

        # --> The layout for the grid in the game.
        def layout_of_grid():
            line1 = "\n-----------\n"
            line2 = f" {grid[0]} | {grid[1]} | {grid[2]}        0 | 1 | 2\n"
            line3 = "-----------\n"
            line4 = f" {grid[3]} | {grid[4]} | {grid[5]}        3 | 4 | 5\n"
            line5 = "-----------\n"
            line6 = f" {grid[6]} | {grid[7]} | {grid[8]}        6 | 7 | 8\n"
            line7 = "-----------\n"
            self.layout = line1 + line2 + line3 + line4 + line5 + line6 + line7
            print(self.layout)

        layout_of_grid()

        def user_check():  # --> Checks if the user has won or lost.
            # VERTICAL ROWS
            if grid[0] == self.choice and grid[3] == self.choice and grid[6] == self.choice:
                print("-------- GAME OVER / YOU WIN! --------\n")
                play_again()
            elif grid[1] == self.choice and grid[4] == self.choice == grid[7] == self.choice:
                print("-------- GAME OVER / YOU WIN! --------\n")
                play_again()
            elif grid[2] == self.choice and grid[5] == self.choice and grid[8] == self.choice:
                print("-------- GAME OVER / YOU WIN! --------\n")
                play_again()
            # HORIZONTAL ROWS
            elif grid[0] == self.choice and grid[1] == self.choice and grid[2] == self.choice:
                print("-------- GAME OVER / YOU WIN! --------\n")
                play_again()
            elif grid[3] == self.choice and grid[4] == self.choice and grid[5] == self.choice:
                print("-------- GAME OVER / YOU WIN! --------\n")
                play_again()
            elif grid[6] == self.choice and grid[7] == self.choice and grid[8] == self.choice:
                print("-------- GAME OVER / YOU WIN! --------\n")
                play_again()
            # DIAGONAL LINES
            elif grid[0] == self.choice and grid[4] == self.choice and grid[8] == self.choice:
                print("-------- GAME OVER / YOU WIN! --------\n")
                play_again()
            elif grid[6] == self.choice and grid[4] == self.choice and grid[2] == self.choice:
                print("-------- GAME OVER / YOU WIN! --------\n")
                play_again()
            elif "-" not in grid:
                print("-------- GAME OVER / DRAW! --------\n")
                play_again()

        user_check()

        def computer_check():  # --> Checks if the computer has won or lost.
            # VERTICAL ROWS
            if grid[0] == var and grid[3] == var and grid[6] == var:
                print("-------- GAME OVER / YOU LOSE! --------\n")
                play_again()
            elif grid[1] == var and grid[4] == var and grid[7] == var:
                print("-------- GAME OVER / YOU LOSE! --------\n")
                play_again()
            elif grid[2] == var and grid[5] == var and grid[8] == var:
                print("-------- GAME OVER / YOU LOSE! --------\n")
                play_again()
            # HORIZONTAL ROWS
            elif grid[0] == var and grid[1] == var and grid[2] == var:
                print("-------- GAME OVER / YOU LOSE! --------\n")
                play_again()
            elif grid[3] == var and grid[4] == var and grid[5] == var:
                print("-------- GAME OVER / YOU LOSE! --------\n")
                play_again()
            elif grid[6] == var and grid[7] == var and grid[8] == var:
                print("-------- GAME OVER / YOU LOSE! --------\n")
                play_again()
            # DIAGONAL LINES
            elif grid[0] == var and grid[4] == var and grid[8] == var:
                print("-------- GAME OVER / YOU LOSE! --------\n")
                play_again()
            elif grid[6] == var and grid[4] == var and grid[2] == var:
                print("-------- GAME OVER / YOU LOSE! --------\n")
                play_again()
            elif "-" not in grid:
                print("-------- GAME OVER / DRAW! --------\n")
                play_again()

        def computers_turn():
            self.valid_coord = list()

            [self.valid_coord.append(i) for i in range(
                len(grid)) if i not in self.numbers_chosen]

            # --> Generates a random valid number.
            random = secrets.choice(self.valid_coord)

            global var
            var = ""

            if self.choice == "x":
                # --> If the user's input is "x", computer uses "o"
                var = "o"
                grid[random] = var
                self.numbers_chosen.append(random)
                print("Computer is picking a coordinate...")
                time.sleep(3)
                layout_of_grid()
                computer_check()
            else:
                # --> If the user's input is "o", computer uses "x"
                var = "x"
                grid[random] = var
                self.numbers_chosen.append(random)
                print("Computer is picking a coordinate...")
                time.sleep(3)
                layout_of_grid()  # --> Prints the progress of the grid.
                computer_check()  # --> checks to make sure nobody has one yet.

        computers_turn()


game = Game()
game.user_choice()

counter = 0
# --> Keeps calling these functions until end of game. (need to change ik, waiting to fix grid)
while counter < 10:
    game.grid_board()
