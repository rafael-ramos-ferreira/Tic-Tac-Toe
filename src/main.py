"""
Tic-Tac-Toe CLI - Your favorite game at the distance of a command

This is a simple tic-tac-toe game to run inside the command-line.

Project elaborated by Rafael Ferreira
"""

# Constants

BOARD_SIZE = 3
NUM_PLAYERS = 2
ICONS = {1: '@', 2: '£', 3: 'X', 4: 'O', 5: '%',
         6: '?', 7: '+', 8: '§', 9: '#', 10: '$'}

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
    """Returns if a specified board field is filled"""
    return not get_house(board, line, column).isspace()


def check_valid_house(line: int, column: int) -> bool:
    """Verifies if a board field is existent"""
    if line >= BOARD_SIZE or column >= BOARD_SIZE:
        return False
    return True


def print_board(board: list) -> None:
    """Gets board string form and prints it"""
    print(board_to_str(board))
    return None


# Score related functions

def score_init() -> dict:
    """Initializes the player's score"""
    player_score_board = {"V1": 0, "V2": 0, "V3": 0, "H1": 0, 
                   "H2": 0, "H3": 0, "CLR": 0, "CRL": 0}
    return player_score_board


def add_score(player_score_board: dict, line: int, column: int) -> None:
    """Tests the position of selected house and add corresponding score"""
    match line:
        case 0:
            if column == 0:
                player_score_board["V1"] += 1
                player_score_board["H1"] += 1
                player_score_board["CLR"] += 1
            elif column == 1:
                player_score_board["V2"] += 1
                player_score_board["H1"] += 1
            elif column == 2:
                player_score_board["V3"] += 1
                player_score_board["H1"] += 1
                player_score_board["CRL"] += 1
        case 1:
            if column == 0:
                player_score_board["V1"] += 1
                player_score_board["H2"] += 1
            elif column == 1:
                player_score_board["V2"] += 1
                player_score_board["H2"] += 1
                player_score_board["CRL"] += 1
                player_score_board["CLR"] += 1
            elif column == 2:
                player_score_board["V3"] += 1
                player_score_board["H2"] += 1
        case 2:
            if column == 0:
                player_score_board["V1"] += 1
                player_score_board["H3"] += 1
                player_score_board["CRL"] += 1
            elif column == 1:
                player_score_board["V2"] += 1
                player_score_board["H3"] += 1
            elif column == 2:
                player_score_board["V3"] += 1
                player_score_board["H3"] += 1
                player_score_board["CLR"] += 1
    return None


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
    player = {"player_score": score_init(), "player_name": "",
              "icon": 'X'}
    return player


def player_name_change(player: dict, name_str: str) -> None:
    """Changes the player name"""
    player["player_name"] = name_str
    return None


def choose_icon(player: dict) -> None:
    """Allows the player to choose an icon"""
    print(ICONS)
    icon = int(input("What's your desired icon? (index) "))
    icon_token = ICONS.get(icon)
    player["icon"] = icon_token
    return None


def get_icon(player: dict) -> chr:
    """Returns the selected player's icon"""
    return player["icon"]


def get_name(player: dict) -> str:
    """Returns the selected player's name"""
    return player["player_name"]


# Play related functions

def get_play(player: dict) -> tuple:
    """Filters the input given in a play"""
    play_input = str(input(f"{get_name(player)} \
                           insert your play (or q to forsake) "))
    input_filtered = play_input.split()
    if (len(input_filtered) > 3):
        raise ValueError("Invalid arguments")
    if input_filtered[0] == "q":
        return (-1, 0)  # flag if the player chose to quit
    elif input_filtered[0] != "p":
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
    players = [player_init(), player_init()]
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
        play = get_play(players[player_index])
        if check_forsake(play):
            give_victory(players[(play_counter + 1) % NUM_PLAYERS])
            break
        line, column = convert_coordinates(play)
        if check_occupied(board, line, column) or not check_valid_house(line, column):
            play_counter += 1
            raise ValueError("Inadequate play!")
        change_value(board, line, column, get_icon(players[player_index]))
        add_score(players[player_index]["player_score"], line, column)
        if check_victory(players[player_index]["player_score"]):
            print_board(board)
            print('\n\n')
            give_victory(players[player_index])
            print('\n\n')
            break
        play_counter += 1
    return None

# Start play call

main()
