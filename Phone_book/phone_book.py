import pickle

with open('names', 'rb') as f:
    names = pickle.load(f)
with open('phones', 'rb') as f:
    phones = pickle.load(f)

def save():
    with open('names', 'wb') as f:
        pickle.dump(names, f)
    with open('phones', 'wb') as g:
        pickle.dump(phones, g)

exit = ""
while exit != "E" and exit != "Exit":

    print()
    msg1 = "Type 'S' to Search a contact"
    msg2 = "Type 'A' to Add a contact"
    msg3 = "Type 'D' to Delete a contact"
    msg4 = "Type 'P' to Print the Phone Book"
    msg5 = "           OR"

    print(msg1 + "\n" + msg5 + "\n" + msg2 + "\n" + msg5 + "\n"  + msg3 + "\n" + msg5 + "\n" + msg4 + "\n")
    action = input("Give a value (Search, Add, Delete, Print) : ")
    print()

    if action == "S" or action == "Search":
        name = input("Give me a name to Search: ")
        if name in names:
            index = names.index(name)
            phone = phones[index]
            print(name + " phone number is: " + phone)
        else:
            print(name + " not found")

    elif action == "A" or action == "Add":
        name = input("Give me a name to Add: ")
        if name not in names:
            names.append(name)
            phone = input("Give me " + name + " phone number: ")
            phones.append(phone)
            save()
            print(name + " Added\n")
        else:
            print(name + " already exists! Give another name.")

    elif action == "D" or action == "Delete":
        name = input("Give me a name to Delete: ")
        if name in names:
            index = names.index(name)
            names.pop(index)
            phones.pop(index)
            save()
            print(name + " Deleted\n")
        else:
            print(name + " not found")

    elif action == "P" or action == "Print":
        print("\nPHONE BOOK \n")
        for i in range(len(names)):
            print(names[i] + " --> " + phones[i])

    print("\n")
    exit = input("Type Exit to finish or press enter to continue: ")
