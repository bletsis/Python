


katalogue = []
print()

for _ in range(3):

    person = {
        "surname": "",
        "name": "",
        "father_name": "",
        "address": "",
        "city": "",
        "code": "",
        "phone1": "",
        "phone2": "",
        "mobile": "",
        "email": "",
    }

    surname = input("Δώσε επίθετο: ")
    person["surname"] = surname
    name = input("Δώσε όνομα: ")
    person["name"] = name
    father_name = input("Δώσε πατρώνυμο: ")
    person["father_name"] = father_name
    print()
    katalogue.append(person)
print()
print(person)

