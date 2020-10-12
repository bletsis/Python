import turtle
import random

x = ""
sum1 = 0
sum2 = 0

player_one = turtle
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-300,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-300,-100)
pen = player_one.clone()
pen.color("black")
pen.shape("square")
pen.hideturtle()

player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-300,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-300,-100)

for i in range(100):
    if player_one.pos() >= (270,100):
        while x != "exit":
            pen.penup()
            pen.goto(-450, 350)
            pen.pendown()
            msg2 = "                 BRAVO!!!!  First Player Wins!"
            pen.color("green")
            pen.write(msg2, font=("Arial Bold", 20))
            pen.penup()
            pen.goto(-450, 310)
            pen.pendown()
            msg2 = "TOTAL SCORE: turtle1 steps:" + str(sum1) + "   turtle2 steps:" + str(sum2)
            pen.write(msg2, font=("Arial Bold", 20))

            pen.penup()
            pen.goto(-450, 200)
            pen.pendown()
            msg3 = "                      TYPE 'exit' to FINISH"
            pen.write(msg3, font=("Arial Bold", 20))
            x = input()
        break
    elif player_two.pos() >= (270,-100):
        while x != "exit":
            pen.penup()
            pen.goto(-450, 350)
            pen.pendown()
            msg1 = "                      BRAVO!!!!  Second Player Wins!"
            pen.color("blue")
            pen.write(msg1, font=("Arial Bold", 20))
            pen.penup()
            pen.goto(-450, 310)
            pen.pendown()
            msg2 = "TOTAL SCORE: turtle1 steps:" + str(sum1) + "   turtle2 steps:" + str(sum2)
            pen.write(msg2, font=("Arial Bold", 20))
            pen.penup()
            pen.goto(-450, 200)
            pen.pendown()
            msg3 = "                      TYPE 'exit' to FINISH"
            pen.write(msg3, font=("Arial Bold", 20))
            x = input()
        break
    else:
        print("\nROUND:", i+1)
        player_one_turn = input("Press 'Enter' to roll the die for the First turtle ")
        die_outcome1 = random.randint(1, 6)
        print("     The result of the die roll for the First turtle is:", die_outcome1)

        sum1 += die_outcome1
        player_one.fd(3*die_outcome1)
        player_two_turn = input("\nPress 'Enter' to roll the die for the Second turtle ")
        die_outcome2 = random.randint(1, 6)
        print("     The result of the die roll for the Second turtle is:", die_outcome2)

        sum2 += die_outcome2
        player_two.fd(3*die_outcome2)