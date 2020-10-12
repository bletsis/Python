import random

feet_in_mile = 5280

bletsis = ["Costis", "Nikos", "Anastasis", "Alexandros"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)

def m_in_km(meters):
    km = meters/1000
    return km