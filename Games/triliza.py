
# Η συνάρτηση σχεδιασμού της τρίλιζας
def print_board():
    print("\n    0   1   2")
    print("  +---+---+---+")
    print("0 | " + board[0][0] + " |" + " " + board[0][1] + " |" + " " + board[0][2] + " |")
    print("  +---+---+---+")
    print("1 | " + board[1][0] + " |" + " " + board[1][1] + " |" + " " + board[1][2] + " |")
    print("  +---+---+---+")
    print("2 | " + board[2][0] + " |" + " " + board[2][1] + " |" + " " + board[2][2] + " |")
    print("  +---+---+---+")

# Έλεγχος για τερματισμό του προγράμματος
test = ""
while test != "q":

# Αρχικοποίηση μεταβλητών
    board = [
             [" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]
    ]
    player = "O"

# Εναλλαγή παικτών
    for _ in range(9):
        print_board()
        if player == "X":
            player = "O"
        else:
            player = "X"

# Επιλογή τετραγώνου από παίκτες και έλεγχος ότι είναι έγκυρη η επιλογή
        while True:
            print("\nPlayer " + player + " plays!")
            print()

            try:
                row = int(input("Give Row: "))
                col = int(input("Give Column: "))
            except:
                print("\nWrong Selection! Please select between 0-2")
                continue
            if row < 0 or row >2:
                print("\nWrong Selection! Please select between 0-2")
                continue
            elif col < 0 or col >2:
                print("\nWrong Selection! Please select between 0-2")
                continue
            elif board[row][col] != " ":
                print("\nPick an empty box!")
                continue
            else:
                board[row][col] = player
                break

# Έλεγχος για συμπλήρωση τριάδων ανά γραμμή
        winner = False
        if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " ":
            winner = player
        elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != " ":
            winner = player
        elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != " ":
            winner = player

# Έλεγχος για συμπλήρωση τριάδων ανά στήλη
        elif board[0][0] == board[1][0] and board[1][0] == board[2] [0] and board[0][0] != " ":
            winner = player
        elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != " ":
            winner = player
        elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != " ":
            winner = player

# Έλεγχος για συμπλήρωση τριάδων ανά διαγώνιο
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
            winner = player
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " ":
            winner = player

# Ανακήρυξη νικητή ή ισοπαλία
        if winner:
            print_board()
            print("\nPlayer " + player + " won!")
            break

    else:
        print_board()
        print("\nIsopalia!")

    test = input("\nType q to Finish or press Enter to continue: ")