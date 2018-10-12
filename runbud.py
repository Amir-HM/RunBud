# imported modules
# time modules for time delays
import time
# webbrowser module to open conversion webpage
import webbrowser
# math module for math function
import math
# random module for randomizing events
import random

# var representing available exercises
exercise_1 = '\t\t\t   Running'
exercise_2 = '\t\t\t   Football'
exercise_3 = '\t\t\t   Cycling'

# var representing the exercises and their MET values
run_exercise = "running"
foot_exercise = "football"
bike_exercise = "cycling"
running_met = 11
foot_met = 9
bike_met = 12

# title
print("\t\t\033[1;32;40m Hello, welcome to RunBud™")

# delay
time.sleep(0.75)

# explain the program
print("\t Calculate calories burned after a workout!")

# delay
time.sleep(0.5)

# printing all the available exercises with delays
print(exercise_1)
time.sleep(0.5)
print(exercise_2)
time.sleep(0.5)
print(exercise_3)
time.sleep(0.75)

# prompt the user to answer what exercise to choose
user_exercise = input("To begin, choose your exercise: ")
# while loop that confirms the users answer
while True:
    if user_exercise == run_exercise:
        print("\t\t   You chose running!")
        break
    elif user_exercise == foot_exercise:
        print("\t\t   You chose football!")
        break
    elif user_exercise == bike_exercise:
        print("\t\t   You chose cycling!")
        break
    else:
        user_exercise == run_exercise
        print("Invalid exercise, please try again.")
        user_exercise = input("Choose your exercise:")

# delay
time.sleep(0.75)

print("\t To continue, please insert data below")
# input time and weight
user_time = float(input("For how long did you exercise (hrs)? "))
# asking if lbs to kg conversion is needed, if so a conversion webpage will appear
convert = input("Would you like to convert lbs to kg?[y/n] ")
if convert == 'y':
    webbrowser.open("https://goo.gl/aWyVvA")
user_weight = float(input("Please insert your current weight (kg): "))

# 1st part of calc
ans = running_met * user_weight


thinking = "\n Using extreme algorithms to calculate data...", "\nConnecting to the NASA quantum supercomputer...", "\nTransmitting asynchronous light rays through the time space continuum..."

# using user data to calculate calories
calories = ans * user_time
time.sleep(0.5)
print(random.choice(thinking))
time.sleep(1)

if calories > 100:
    print("\nGood job, you successfully burned",calories,"calories during your workout!")
elif calories < 100:
        print("\nYou successfully burned",calories,"calories, don't worry theres always a tomorrow!")
