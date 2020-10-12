MyUniqueList = []
MyLeftovers = []


def add(value):
    if value not in MyUniqueList:
        MyUniqueList.append(value)
        print(True)
    else:
        left(value)


def left(value):
    MyLeftovers.append(value)
    print(False)


add(3)
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()

add(3)
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()

add(5)
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()

add(3)
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()

add(3)
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()

add(0)
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()

add(2)
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()

add("Hi")
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()

add("Hi")
print("MyUniqueList:")
print(MyUniqueList)
print("MyLeftovers:")
print(MyLeftovers)
print()