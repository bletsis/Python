#########################################################
#  0     1     2     3     4     5    6    7    8   9   #
#########################################################
#  1     2     3     4     5     6    7    8    9   10  #
#########################################################
# -10   -9    -8    -7    -6    -5   -4   -3   -2  -1   #
#########################################################

test = ""
while test != "exit":

    list1 = []

    for i in range(10):
        o = int(input("enter one number: "))
        list1.append(o)



    max1 = list1[0]
    for element in list1:
        if max1 < element:
            max1 = element

    list2 = list1[-10:-5]

    list3 = list1

    print("\nthe biggest number is: ", max1)
    print("\nThe numbers from 5-8:", list1[4:8])
    print("\nThe numbers from 1-5:", list1[-10:-5])
    print("\nThe numbers from 1-5 with unselected the other 5 numbers:", list2)
    print("\nThe numbers from list1 coped to list 3:", list3)
    test = input("\ntype exit to finnish program or press enter to continue: ")