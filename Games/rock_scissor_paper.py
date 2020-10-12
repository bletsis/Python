from random import randrange

# Δημιουργώ μία λίστα για τον έλεγχο όλων των δυνατών επιλογών του χρήστη.
choice = ["Rock", "Scissor", "Paper", "Exit", "R", "S", "P", "E"]

# cnt1: μετρητής επιτυχιών παίκτη, cnt2: μετρητής επιτυχιών υπολογιστή,
# round: μετρητής γύρων history: λίστα που αποθηκεύεται το ιστορικό του παιχνιδιού
cnt1 = 0
cnt2 = 0
round = 1
history = []
player = input("\nGive your name: ")


# Εκτύπωση ιστορικού παιχνιδιού
def print_history():
    print("\n                                GAME HISTORY")
    print("                                ------------")
    for record in history:
        print(record)


while True:
    x = input("\n" + player + " type your choice ([R]ock or [S]cissor or [P]aper) or [E]xit to exit: ")
    # Έλεγχος εγκυρότητας της εισαγωγής του παίκτη
    while x not in choice:
        x = input("\n" + player + " wrong choice!\nPlease type your choice \
                 ([R]ock or [S]cissor or [P]aper) or [E]xit to exit: ")

    # Μετατροπή των σύντομων εισαγωγών σε πλήρεις
    if x == "R":
        x = "Rock"
    elif x == "S":
        x = "Scissor"
    elif x == "P":
        x = "Paper"
    elif x == "E":
        x = "Exit"
        break

    # Παραγωγή τυχαίας επιλογής από τον η/υ από τα 3 πρώτα στοιχεία της λίστας choice
    z = randrange(3)
    y = choice[z]
    print("\nRound: " + str(round) + "\n" + player + " choice: " + x + "\nComputer choice: " + y)

    # Έλεγχος για νικητή
    if x == "Rock" and y == "Scissor":
        print(x + " beats " + y)
        cnt1 += 1
    elif x == "Scissor" and y == "Paper":
        print(x + " beats " + y)
        cnt1 += 1
    elif x == "Paper" and y == "Rock":
        print(x + " beats " + y)
        cnt1 += 1
    elif x == y:
        print("Draw")
    else:
        print(y + " beats " + x)
        cnt2 += 1

    # Προσθήκη στη λίστα του ιστορικού των δεδομένων του γύρου
    history.append("Round " + str(round) + ":      " + player + ": " + (x + "\t").expandtabs(15) \
                   + "Computer: " + (y + "\t").expandtabs(15) + "Score: " + str(cnt1) + "-" + str(cnt2))
    round += 1

    # Εκτύπωση αποτελεσμάτων γύρου
    print(player + ": " + str(cnt1) + "   Computer: " + str(cnt2))
    print("*******************************************************************************")

    # Έλεγχος αν έχουν επιτευχθεί 3 νίκες για τον τερματισμό του παιχνιδιού
    if cnt1 == 3:
        print("\n" + player + " Won!")
        h = input("Press H to see Game History OR Enter to Exit: ")
        if h == "H":
            print_history()
        break
    elif cnt2 == 3:
        print("\n" + "Computer Won!")
        h = input("Press H to see Game History OR Enter to Exit: ")
        if h == "H":
            print_history()
        break
