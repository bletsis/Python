pencils = input("Give the number of pencils: ")
koutes = int(pencils)//180
koutia = (int(pencils)%180)//12
pencils = int(pencils) - koutes * 180 - koutia * 12
print("To apotelesma einai: " + str(koutes) + " koutes, " + str(koutia) + " koutia " + "& " + str(pencils) + " molibia.")