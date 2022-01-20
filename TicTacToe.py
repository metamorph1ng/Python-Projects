

# Dictionary = {"1": "1", "2": "2", "3": "3", "4": "4",
#              "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}

# Tic Tac Toe Board


def Board(arg):
    print("|" + arg["1"] + "|" + arg["2"] +
          "|" + arg["3"] + "|")
    print("_______")
    print("|" + arg["4"] + "|" + arg["5"] +
          "|" + arg["6"] + "|")
    print("_______")
    print("|" + arg["7"] + "|" + arg["8"] +
          "|" + arg["9"] + "|")
# Board()


def PickXO():
    while True:
        XO_input = input("Player 1, please  pick and then enter X or O: ")
        if XO_input not in ["X", "x", "O", "o"]:
            print("Please pick X or O")
        elif XO_input in ["X", "x"]:
            return "X"
        else:
            return "O"


# PickXO()


def P2_XO_Pick(arg):
    if arg == "X":
        return "O"
    else:
        return "X"


def Player_Move(arg):
    while True:
        Move = input("Pick a number 1 through 9 from the Dictionary.")
        if arg[Move] == "X" or arg[Move] == "O":
            print(
                "The selected number has already been used. Please choose another number.")
            continue
        elif Move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Please input a number corresponding to Dictionary.")
        else:
            return Move

# Player_Move()


def Check_Win(arg):
    if (arg["1"] == "X" and arg["2"] == "X" and arg["3"] == "X") or (arg["4"] == "X" and arg["5"] == "X" and arg["6"] == "X") or (arg["7"] == "X" and arg["8"] == "X" and arg["9"] == "X") or (arg["1"] == "X" and arg["4"] == "X" and arg["7"] == "X") or (arg["2"] == "X" and arg["5"] == "X" and arg["8"] == "X") or (arg["3"] == "X" and arg["6"] == "X" and arg["9"] == "X") or (arg["1"] == "X" and arg["5"] == "X" and arg["9"] == "X") or (arg["3"] == "X" and arg["5"] == "X" and arg["7"] == "X"):
        return True
    elif (arg["1"] == "O" and arg["2"] == "O" and arg["3"] == "O") or (arg["4"] == "O" and arg["5"] == "O" and arg["6"] == "O") or (arg["7"] == "O" and arg["8"] == "O" and arg["9"] == "O") or (arg["1"] == "O" and arg["4"] == "O" and arg["7"] == "O") or (arg["2"] == "O" and arg["5"] == "O" and arg["8"] == "O") or (arg["3"] == "O" and arg["6"] == "O" and arg["9"] == "O") or (arg["1"] == "O" and arg["5"] == "O" and arg["9"] == "O") or (arg["3"] == "O" and arg["5"] == "O" and arg["7"] == "O"):
        return True
# Check_Win()


def Check_Draw(arg):
    if (arg["1"] == ("X") or arg["1"] == ("O")) and (arg["2"] == ("X") or arg["2"] == ("O")) and (arg["3"] == ("X") or arg["3"] == ("O")) and (arg["4"] == ("X") or arg["4"] == ("O")) and (arg["5"] == ("X") or arg["5"] == ("O")) and (arg["6"] == ("X") or arg["6"] == ("O")) and (arg["7"] == ("X") or arg["7"] == ("O")) and (arg["8"] == ("X") or arg["8"] == ("O")) and (arg["9"] == ("X") or arg["9"] == ("O")):
        return True
# Check_Draw


def Play_Again():
    while True:
        Play_again_input = input("Would you like to play again? Enter Y or N")
        if Play_again_input not in ["Y", "y", "N", "n"]:
            print("Please enter Y or N")
        elif Play_again_input == ("Y") or Play_again_input == ("y"):
            return True
        elif Play_again_input == ("N") or Play_again_input == ("n"):
            return False
# Play_Again()


def Game_On():

    Dictionary = {"1": "1", "2": "2", "3": "3", "4": "4",
                  "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
    print("Welcome to TicTacToe!")
    print("Player 1 please pick X or O.")
    P1_XO = PickXO()
    P2_XO = P2_XO_Pick(P1_XO)
    print("Player 1 will be {} and Player 2 will be {}.".format(P1_XO, P2_XO))
    print("\n"*1)
    Play = True
    while Play:
        Board(Dictionary)
        print("\n"*1)
        print("Player 1's turn.")
        P1_Move = Player_Move(Dictionary)
        Dictionary[P1_Move] = P1_XO
        print("\n"*1)
        Board(Dictionary)
        print("\n"*1)
        if Check_Win(Dictionary) is True:
            print("Player 1 has Won!")
            break
        elif Check_Draw(Dictionary) is True:
            print("It's a draw.")
            break
        print("Player 2's turn.")
        P2_Move = Player_Move(Dictionary)
        Dictionary[P2_Move] = P2_XO
        print("\n"*1)
        if Check_Win(Dictionary) is True:
            print("Player 2 has Won!")
            break
        elif Check_Draw(Dictionary) is True:
            print("It's a Draw.")
            Play = False
    Play_Again_ = Play_Again()
    if Play_Again_ is True:
        Game_On()
        print("A new game will begin!")
    else:
        print("Thank you for playing TicTacToe! :)")


Game_On()
