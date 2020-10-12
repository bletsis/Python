def check_for_number():
    while True:
        num = input("Please enter a number: ")
        try:
            val = int(num)
            return val
            break;
        except:
            try:
                val = float(num)
                return val
                break;
            except:
                print("This is not a number! Please enter a valid number.")


num = check_for_number()
result = num
print(result)
