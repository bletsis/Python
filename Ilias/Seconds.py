def dok(num):
    test = num.replace(".", "", 1)
#    test = test.replace("-", "", 1)
    return test

hours = input("\nHow many Hours do you want: ")
while not dok(hours).isdigit():
    hours = input("\nHow many Hours do you want: ")

minutes = input("\nHow many Minutes do you want: ")
while not dok(minutes).isdigit():
    minutes = input("\nHow many Minutes do you want: ")

seconds = input("\nHow many Seconds do you want: ")
while not dok(seconds).isdigit():
    seconds = input("\nHow many Seconds do you want: ")

hours_in_seconds = float(hours) * 3600
minutes_in_seconds = float(minutes) * 60
seconds2 = hours_in_seconds + minutes_in_seconds + float(seconds)
print("\nYou enter " +  str(hours) +  ' Hours and ' + str(minutes) + " Minutes and " + seconds + " Seconds converting all of them in Seconds we have " + str(seconds2) + " Seconds. ")
