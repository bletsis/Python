name = input("What is your name: ")

# ***********************************************************
# * Check if grade_in_essay is not string or not >20 or <0  *
# ***********************************************************

grade_in_essay = input("What is your grade in Essay: ")
while not grade_in_essay.replace(".","",1).isdigit() or float(grade_in_essay) <0 or float(grade_in_essay) > 20:
    grade_in_essay = input("Give a grade between 0-20. What is your grade in Essay: ")

grade_in_history = input("What is your grade in History: ")
while not grade_in_history.replace(".","",1).isdigit() or float(grade_in_history) <0 or float(grade_in_history) > 20:
    grade_in_history = input("Give a grade between 0-20. What is your grade in History: ")

grade_in_math = input("What is your grade in Math: ")
while not grade_in_math.replace(".","",1).isdigit() or float(grade_in_math) <0 or float(grade_in_math) > 20:
    grade_in_math = input("Give a grade between 0-20. What is your grade in Math: ")

grade_in_geography = input("What is your grade in Geography: ")
while not grade_in_geography.replace(".","",1).isdigit() or float(grade_in_geography) <0 or float(grade_in_geography) > 20:
    grade_in_geography = input("Give a grade between 0-20. What is your grade in Geography: ")

oros = float(grade_in_essay) + float(grade_in_history) + float(grade_in_math) + float(grade_in_geography)
mesos_oros = oros / 4

mikos_name = len(name)
mikos_essay = len(grade_in_essay)
mikos_history =len(grade_in_history)
mikos_math = len(grade_in_math)
mikos_geography = len(grade_in_geography)
mikos_mo = len(str(mesos_oros))
a = 23 - mikos_name
b = 43 - mikos_essay
c = 43 - mikos_history
d = 43 - mikos_math
e = 43 - mikos_geography
f = 34 - mikos_mo


print("*****************************************************************")
print("*                                                               *")
print("*           The Grades of student: " + name.upper() + ", are:" + a*" " + "*")
print("*                                                               *")
print("*   ESSAY      :     " + grade_in_essay + b*" " + "*")
print("*   HISTORY    :     " + grade_in_history + c*" " + "*")
print("*   MATH       :     "+ grade_in_math + d*" " + "*")
print("*   GEOGRAPHY  :     "+ grade_in_geography +e*" " + "*")
print("*                                                               *")
print("*      The Average Grade is : " + str(mesos_oros) + f*" " + "*")
print("*                                                               *")
print("*****************************************************************")