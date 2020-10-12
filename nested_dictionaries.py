from random import randrange
family = {
    "father": {
        "name": "Costis Bletsis",
        "occupation": "IT",
        "drinks": ["Ouzo", "Beer", "Wine", "Votka", "Whisky", "Rum"]
    },
    "mother": {
        "name": "Sofia Kapoutseli",
        "occupation": "Teacher",
        "drinks": [
            "Amaretto", "Beer", "Raki", "Soda"]
    },
    "children": [
        {
            "name": "Nikos Bletsis",
            "drinks": ["Beer", "Amaretto", "Wine", "Votka", "Whisky", "Tsipouro"]
        },
        {
            "name": "Anastasis Bletsis",
            "drinks": ["Beer", "Wine", "Votka", "Whisky"]
        },
        {
            "name": "Alexandros Bletsis",
            "drinks": ["Beer", "Wine", "Votka", "Orange", "Coca_cola"]
        }
    ]
}

print()
print(family["father"]["name"] + " drinks: " + family["father"]["drinks"][randrange(len(family["father"]["drinks"]))])
print()
print(family["mother"]["name"] + " drinks: " + family["mother"]["drinks"][randrange(len(family["mother"]["drinks"]))])

for i in range(len(family["children"])):
    print()
    print(family["children"][i]["name"] + " drinks: " + family["children"][i]["drinks"][randrange(len(family["children"][i]["drinks"]))])
