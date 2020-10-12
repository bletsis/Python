import random

# Συνάρτηση που αφαιρεί αρνητικό πρόσιμο και υποδιαστολή από την εισαγωγή του χρήστη.
def dok(choice_position):
    test = choice_position.replace(".", "", 1)
    test = choice_position.replace("-", "", 1)
    return test

# Συνάρτηση για την εκτύπωση της κατάστασης
def panel():
    for position in range(n):
        if state[position] == 0:
            print("_", end="")
        elif state[position] == 1:
            print(numbers[position], end="")
        else:
            print(numbers[position], end="")
    print("\n")

# Πλήθος στοιχείων για ταίριασμα
n = 10

# Αρχικοποίηση της λίστας με τις n τυχαίες επιλογές
numbers = []

for i in range(int(n/2)):
    num = random.randint(0, 9)
    numbers.append(num)
numbers.extend(numbers)
random.shuffle(numbers)

# Αρχικοποίηση της λίστας κατάστασης των επιλογών με όλες τις επιλογές κλειστές
# Η κωδικοποίηση των επιλογών
# 0 = closed
# 1 = open
# 2 = temp_open
state = []
for i in range(n):
    state.append(0)

# ΑΡΧΗ ΕΚΤΕΛΕΣΗΣ ΤΟΥ ΠΡΟΓΡΑΜΜΑΤΟΣ

active = True
found = 0
score = 0
print()

while active:
    score +=1

# ΕΙΣΑΓΩΓΗ 1ης ΕΠΙΛΟΓΗΣ

# Έλεγχος αν η τιμή είναι ακέραιος αριθμός εντός των ορίων της λίστας που να μην είναι ανοιχτός.
    choice1_position = input("Give position of 1st Number (0-" + str(n - 1) + "): ")
    while not dok(choice1_position).isdigit() or int(choice1_position) < 0 or\
            int(choice1_position) >= n or state[int(choice1_position)] == 1:
        print("Wrong input! Please try again.\n")
        choice1_position = input("Give position of 1st Number (0-" + str(n - 1) + "): ")

# ΕΙΣΑΓΩΓΗ 2ης ΕΠΙΛΟΓΗΣ

# Έλεγχος αν η τιμή είναι ακέραιος αριθμός εντός των ορίων της λίστας,
# που να μην είναι ανοιχτός και να μην είναι ίδιος με την 1η επιλογή.
    choice2_position = input("Give position of 2nd Number (0-" + str(n - 1) + "): ")
    while not dok(choice2_position).isdigit() or int(choice2_position) < 0 or\
            int(choice2_position) >= n or state[int(choice2_position)] == 1 or\
            int(choice2_position) == int(choice1_position):
        print("Wrong input! Please try again.\n")
        choice2_position = input("Give position of 2nd Number (0-" + str(n - 1) + "): ")
    print("\nYou have selected:\n1st number position: " + choice1_position + "\n2nd number position: " + choice2_position)

    choice1_position = int(choice1_position)
    choice2_position = int(choice2_position)

# Αλλλάζουμε την κατάσταση των δύο επιλογών μας σε temp_open = 2
    state[choice1_position] = 2
    state[choice2_position] = 2
    print()
# Τυπώνουμε την τρέχουσα κατάσταση
    panel()

# Ελέγχουμε αν το στοιχείο της 1ης επιλογής είναι το ίδιο με το στοιχείο της 2ης επιλογής
    if numbers[choice1_position] == numbers[choice2_position]:
        state[choice1_position] = 1
        state[choice2_position] = 1
        print("Success!")
        found += 2
        if found == n:
            print("\nBravo!\n\nGAME FINNISHED!  Score = " + str(score))
            active = False
    else:
        state[choice1_position] = 0
        state[choice2_position] = 0
        print("Failure!")

    panel()



