def dok(num):
    test = num.replace(".", "", 1)
    test = test.replace("-", "", 1)
    return test


num = input("Give a Number: ")
while not dok(num).isdigit():
    num = input("\nGive a Number: ")
print()
print(num)
