exit = ""
cash_desk = []
while exit != "E":
    key = input("\nType 'A' to Add a new person or 'R' to Remove or 'P' to Print or 'E' to Exit : ")
    if key == "A":
        person = input("\nGive a Name to add: ")
        cash_desk.append(person)
        print(person + " added")
    elif key == "R":
        if len(cash_desk) == 0:
            print("\nQueue is Empty! Please select between 'A' Add, 'P' Print, 'E' Exit")
        else:
            person = cash_desk.pop(0)
            print(person + " served")
    elif key == "P":
        print("\nThe queue is : " + str(cash_desk))
    elif key == "E":
        exit = "E"
    else:
        print("\nWrong key! Select between 'A' Add, 'R' Remove, 'P' Print, 'E' Exit")

