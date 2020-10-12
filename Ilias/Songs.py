#exit = ""
active = True
songs = []
#while exit != "E":
while active:
    key = input("\nType:\n 'A' to Add a new song title,\n 'R' to Remove an existing song title,\n 'P' to Print all song titles,\n'SA' to Sort song titles in Ascending order,\n'SD' to Sort song titles in Descending order,\n 'E' to Exit: ")
    if key == "A":
        song = input("\nGive a song title to add: ")
        if song not in songs:
            songs.append(song)
            print(song + " added")
        else:
            print(("The title already exist"))
    elif key == "R":
        song = input("\nGive song title to Remove: ")
        if song in songs:
            songs.remove(song)
            print(song + " removed")
        else:
            print("Song title not in list")
    elif key == "P":
        print("\nThe saved song titles are: " + str(songs))
    elif key == "SA":
        songs.sort()
    elif key == "SD":
        songs.sort()
        songs.reverse()
    elif key == "E":
        #exit = "E"
        active = False
    else:
        print("\nWrong key! Select between 'A' Add, 'R' Remove, 'P' Print, 'SA' Ascending Sort, SD Descending Sort, 'E' Exit")

