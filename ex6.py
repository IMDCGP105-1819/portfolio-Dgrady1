import time #importing time to make it look like the program is calculating data
name = str(input("Please input your name: "))
age = int(input("Please input your age: "))
height = int(input("Please input your height(please input in centimeters): "))
weight = int(input("Please input your weight(in kilograms): "))
eye_colour = str(input("Please input your eye coloyr: "))
hair_colour = str(input("Please input your hair colour: "))

print("Welcome!", name, "to the program")
time.sleep(2)
print("this program will evaluate you based off of your age, height and weight")
time.sleep(2)
print("So you are", age,"years old")
time.sleep(2)
if age >= 50:
    print("Wow you must have alot of experience with the", age,"years of life you have experienced")
else:
    print("you still must have alot to learn about life, after only being", age, "years old!")
time.sleep(2)
print("So you weigh", weight, "kilograms")
time.sleep(2)
if weight >= 100:
    print("maybe you should hit the gym if you weigh over,", weight, "kilograms")
else:
    print("Wow you are in peak physical condition to weigh", weight, "kilograms")
time.sleep(2)
print("so you are", height, "centimeters tall")
if height >= 182:
    print("Wow you are really tall for", height, "centimeters")
else:
    print("Arn't you a little short?")
time.sleep(2)
print("thankyou for using this program...")
