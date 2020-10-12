numbers =[]
for i in range(10):
    number = float(input("\nGive a number: "))
    numbers.append(number)
print()

maximum = numbers[0]
for num in numbers:
    if num>maximum:
        maximum = num
print(maximum,"\n")

for i in range(4, 8):
    print(numbers[i])

print()

for i in range(-10, -5):
    print(numbers[i])
print()

print(numbers[:5])