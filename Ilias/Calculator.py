test = ""
while test != "exit":

    number1 = input("Give me the first number: ")
    while not number1.isdigit():
        number1= input("Plz enter only numbers" )

    z = input("Give me a symbol: ")
    while z != "+" and z != "-" and z != "*" and z != "/" and z != "//" and z != "%" :
           z = input("Plz enter only + or - or * or  / or  //  or  % ")

    number2 = input("Give me the second number: ")
    while not number2.isdigit():
        number2= input("Plz enter only numbers" )

    if z == "+":
        apotelesma = float(number1) + float(number2)
        print(str(number1) +" + " + str(number2) +" = " + str(apotelesma))


    elif z == "-":
        apotelesma1 = float(number1) - float(number2)
        print(str(number1) +" - " + str(number2) +" = " + str(apotelesma1))


    elif z == "*":
        apotelesma2 = float(number1) * float(number2)
        print(str(number1) +" * " + str(number2) +" = " + str(apotelesma2))


    elif z == "/":
        apotelesma3 = float(number1) / float(number2)
        print(str(number1) +" / " + str(number2) +" = " + str(apotelesma3))


    elif z == "//":
        apotelesma4 = float(number1) // float(number2)
        print(str(number1) +" // " + str(number2) +" = " + str(apotelesma4))


    elif z == "%":
        apotelesma5 = float(number1) % float(number2)
        print(str(number1) +" % " + str(number2) +" = " + str(apotelesma5))
    test = input("type exit to finnish program or press enter to continiue ")
