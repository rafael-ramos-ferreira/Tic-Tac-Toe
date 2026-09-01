"""
Tic-Tac-Toe CLI - Your favorite game at the distance of a command

This is a simple tic-tac-toe game to run inside the command-line.

Project elaborated by Rafael Ferreira
"""

# Constants

BOARD_SIZE = 3
NUM_PLAYERS = 2
ICONS = {1: 'X', 2: 'O', 3: '@', 4: '£', 5: '%',
         6: '?', 7: '+', 8: '§', 9: '#', 10: '$'}
NUM_ICONS = 10
# Board related functions

def board_init() -> list:
    """Initializes the board as a list of lists"""
    board = [[" " for x in range(0,BOARD_SIZE)] for y in range(0, BOARD_SIZE)]
    return board


def board_to_str(board: list) -> str:
    """Converts the board into a string"""
    boarders = f"+{"".join(['-' for x in range(0, BOARD_SIZE * 4 - 3)])}+"
    board_str = ""
    board_str += boarders + "\n"

    for i in range(0, BOARD_SIZE):
        if i != 0:
            board_str += "-" * (BOARD_SIZE * 4 - 1)
            board_str += "\n"
        for j in range(0, BOARD_SIZE):
            board_str += f"{board[i][j]:^3}"
            if j != (BOARD_SIZE-1):
                board_str += "|"
        if i != (BOARD_SIZE-1):
            board_str += "\n"
    board_str += "\n" + boarders
    return board_str


def convert_coordinates(house: tuple) -> tuple: 
    """Converts the coordinates from 1-based (user) to 0-based (board)"""
    x = house[0] - 1
    y = house[1] - 1
    return (x, y)


def change_value(board: list, line: int, column: int, value: any) -> None:
    """Assigns a value to a specified board field"""
    board[line][column] = str(value)
    return None


def get_house(board: list, line: int, column: int) -> str:
    """Returns the value of a specified board field"""
    return board[line][column]


def check_occupied(board: list, line: int, column: int) -> bool:
    """Returns True if a specified board field is filled"""
    return not get_house(board, line, column).isspace()


def check_valid_house(line: int, column: int) -> bool:
    """Verifies if a board field is existent"""
    if (line >= BOARD_SIZE or column >= BOARD_SIZE or 
        line < 0 or column < 0):
        return False
    return True


def print_board(board: list) -> None:
    """Gets board string form and prints it"""
    print(board_to_str(board))
    return None


# Score related functions

def score_init(size: int) -> dict:
    """Initializes the player's score

        - This system works by adding in each play the value of the play to
        the corresponding player, and when the value reaches the size of the
        board, the victory is achieved.
    """
    scores = {}
    for i in range(size):
        scores[f"H{i}"] = 0
        scores[f"V{i}"] = 0
    scores["DLR"] = 0
    scores["DRL"] = 0
    return scores


def add_score(scores: dict, line: int, column: int, size: int) -> None:
    """Tests the position of selected house and add corresponding score"""
    scores[f"H{line}"] += 1
    scores[f"V{column}"] += 1
    if line == column:
        scores["DLR"] += 1          # Diagonal Left-to-Right
    if line + column == size - 1:
        scores["DRL"] += 1          # Diagonal Right-to-Left


# End-game related functions

def check_victory(scores: dict) -> bool:
    """Checks if provided scores correspond to a win"""
    for key in scores:
        if scores[key] == BOARD_SIZE:
            return True
    return False


def check_forsake(house: tuple) -> bool:
    """Checks if current play translates into a forsake"""
    if house[0] == -1:
        return True
    return False


def give_victory(player: dict) -> None:
    """Gives the victory to assigned player"""
    print(f"Player {get_name(player)} has won!")
    return None


def give_tie() -> None:
    """Rules the current game as a tie"""
    print("No player has become victorious!")
    return None


# Player related functions

def player_init() -> dict:
    """Initializes the player dictionary"""
    player = {"player_score": score_init(BOARD_SIZE), "player_name": "",
              "icon": 'X'}
    return player


def player_name_change(player: dict, name_str: str) -> None:
    """Changes the player name"""
    player["player_name"] = name_str
    return None


def choose_icon(player: dict) -> None:
    """Allows the player to choose an icon"""
    print(ICONS)
    while True:
        try:
            icon = int(input("What's your desired icon? (index) "))
        except ValueError:
            print("Incorrect argument! Choose again!")
            continue
        if (icon > NUM_ICONS or icon < 1):
            print("Incorrect argument! Choose again!")
            continue
        break
    icon_token = ICONS.get(icon)
    player["icon"] = icon_token
    return None


def get_icon(player: dict) -> chr:
    """Returns the selected player's icon"""
    return player["icon"]


def get_name(player: dict) -> str:
    """Returns the selected player's name"""
    return player["player_name"]


def get_scores(player: dict) -> dict:
    """Returns the selected player's scoreboard"""
    return player["player_score"]


# Play related functions

def get_play(player: dict) -> tuple:
    """Filters the input given in a play"""
    play_input = ( 
        str(input(f"{get_name(player)} insert your play (or q to forsake) "))
    )
    input_filtered = play_input.split()
    arguments = len(input_filtered)
    if (arguments < 1 or arguments > 3):
        raise ValueError("Invalid arguments")
    if input_filtered[0] == "q":
        return (-1, 0)              # flag if the player chose to quit
    elif (input_filtered[0] != "p" or arguments != 3):
        raise ValueError("Invalid arguments")
    else:
        if (not input_filtered[1].isdigit()
            or not input_filtered[2].isdigit()):
            raise ValueError("Invalid arguments")
        line, column = int(input_filtered[1]), int(input_filtered[2])
        return (line, column)


# Game function

def main() -> None:
    """Runs the game"""
    players = [player_init() for _ in range(0, NUM_PLAYERS)]
    play_counter = 0
    for i in range(0, NUM_PLAYERS):
        name = str(input(f"What's the name of player {i}? "))
        player_name_change(players[i], name)
        choose_icon(players[i])
    board = board_init()
    
    while True:
        if play_counter >= (BOARD_SIZE ** 2):
            give_tie()
            break
        print_board(board)
        player_index = (play_counter) % NUM_PLAYERS
        while True:
            try:
                play = get_play(players[player_index])
            except ValueError as error:
                print(f"Error: {error}. Try again!")
                continue

            if check_forsake(play):
                give_victory(players[(play_counter + 1) % NUM_PLAYERS])
                return None
            line, column = convert_coordinates(play)
            if not check_valid_house(line, column) or check_occupied(board, line, column):
                print("Inadequate play! Try again!")
                continue
            break
        
        change_value(board, line, column, get_icon(players[player_index]))
        add_score(get_scores(players[player_index]), line, column, BOARD_SIZE)
        if check_victory(get_scores(players[player_index])):
            print_board(board)
            print('\n\n')
            give_victory(players[player_index])
            print('\n\n')
            break
        play_counter += 1
    return None

# Start play call (if not imported)

if __name__ == "__main__":
    main()
