pinakas2d = []
row = int(input("Give the num of Rows: "))
col = int(input("Give the num of Cols: "))
for i in range(row):
    pinakas2d.append([])
    for j in range(col):
        element = int(input("Give " + str(i) + "," + str(j) + " element: "))
        pinakas2d[i].append(element)
print(pinakas2d)
