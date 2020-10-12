def check_for_number():
    while True:
        num = input("Please enter a number: ")
        try:
            val = int(num)
            return val
            break;
        except ValueError:
            try:
                val = float(num)
                return val
                break;
            except ValueError:
                print("This is not a number! Please enter a valid number.")


num = check_for_number()
result = num + 100
print(result)
