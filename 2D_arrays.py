# Αρχικοποίηση των δύο πινάκων
array2dA = []
array2dB = []

# Εισαγωγή επιθυμητών γραμμών και στηλών των δύο πινάκων
row = int(input("\nGive the num of Rows: "))
col = int(input("Give the num of Cols: "))
print()

# Επαναλήψεις για δημιουργία γραμμών πίνακα
for i in range(row):

    # Προσθήκη μιας κενής λίστας (γραμμή) στον πίνακα Α
    array2dA.append([])

    # Δημιουργία μιας κενής λίστας για τον πίνακα Β
    new_row = []

    # Επαναλήψεις για δημιουργία στηλών
    for j in range(col):

        # Εισαγωγή από τον χρήστη των στοιχείων του πίνακα
        element = int(input("Give " + str(i) + "," + str(j) + " element: "))

        # Προσθήκη των στοιχείων μέχρι να συμπληρωθούν όλες οι στήλες της γραμμής των πινάκων Α και Β
        array2dA[i].append(element)
        new_row.append(element)

    # Προσθήκη όλης της συμπληρωμένης γραμμής στον πίνακα Β
    array2dB.append(new_row)

# Εκτύπωση όλου του πίνακα Α σε μία γραμμή
print("\nArray A:")
print(array2dA)

#  Εκτύπωση του πίνακα Β κατά γραμμές
print("\nArray B:")
for row in array2dB:
    print(row)

#  Εκτύπωση του πίνακα Β κατά στοιχείο
print("\nArray B:")
for row in array2dB:
    for element in row:
        print(str(element) + " ", end="")
    print()