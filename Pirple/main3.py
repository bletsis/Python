#******************************************************************************************
#*                                                                                        *
#*  A function that accepts 3 parameters and checks for equality between any two of them  *
#*                                                                                        *
#******************************************************************************************

def compare(val1, val2, val3):
    if val1 == val2 or val1 == val3 or val2 == val3 or val1 == val2 == val3:
        test = "True"
    else:
        test = "False"
    return test

result = compare(7, int("5"), 5)
print(result)
