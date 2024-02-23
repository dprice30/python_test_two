from datetime import date

#Decisions at the Crossroad
#Code Correction 

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#The Story Brancher
#Task One: Code Correction

choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")

#The Greatest Showdown
#Task One: Identify the Greatest

num1 = float(input("Enter a number 1: "))
num2 = float(input("Enter a number 2: "))
num3 = float(input("Enter a number 3: "))

if((num1 > num2) and (num1 > num3)):
    print(num1, " is the greatest")
elif((num2 > num1) and (num2 > num3)):
    print(num2, " is the greatest")
elif((num3 > num2) and (num3 > num1)):
    print(num3, " is the greatest")
elif((num1 == num2) or (num1 == num3) or (num2 == num3)):
    print("Two or more numbers are equal!")

#Task Two: Identify the Smallest

num1 = float(input("Enter a number 1: "))
num2 = float(input("Enter a number 2: "))
num3 = float(input("Enter a number 3: "))

if((num1 > num2) and (num1 > num3)):
    print(num1, " is the greatest!") 
elif((num2 > num1) and (num2 > num3)):
    print(num2, " is the greatest!")
elif((num3 > num2) and (num3 > num1)):
    print(num3, " is the greatest!")   
elif((num1 == num2) or (num1 == num3) or (num2 == num3)):
    print("Two or more numbers are equal!")

if((num1 < num3) and (num1 < num2)):
        print(num1, " is the smallest!")
elif((num2 < num1) and (num2 < num3)):
        print(num2, " is the smallest!")
elif((num3 < num1) and (num3 < num2)):
        print(num3, " is the smallest!")

#Task Three: Equality Check

num1 = float(input("Enter a number 1: "))
num2 = float(input("Enter a number 2: "))
num3 = float(input("Enter a number 3: "))

if((num1 > num2) and (num1 > num3)):
    print(num1, " is the greatest!") 
elif((num2 > num1) and (num2 > num3)):
    print(num2, " is the greatest!")
elif((num3 > num2) and (num3 > num1)):
    print(num3, " is the greatest!")   
if((num1 < num3) and (num1 < num2)):
        print(num1, " is the smallest!")
elif((num2 < num1) and (num2 < num3)):
        print(num2, " is the smallest!")
elif((num3 < num1) and (num3 < num2)):
        print(num3, " is the smallest!")
if((num1 == num2) and (num1 == num3) and (num2 == num3)):
    print("All numbers are equal!")
elif((num1 == num2) and (num1 > num3) or (num1 == num3) and (num1 > num2) or (num2 == num3) and (num2 > num1)-9):
    print("Two numbers are equal and the largest")
elif((num1 == num2) and (num1 < num3) or (num1 == num3) and (num1 < num2) or (num2 == num3) and (num2 < num1)):
    print("Two numbers are equal but are not the largest!")

#Leap Year Explorer
#Task One and Two: Leap Year Checker and Century Verification

year = int(input("Enter year using 4 digits: "))

if(year % 4 == 0 and year % 10 == 0):
    print("Leap and century year!")
elif(year % 4 == 0 and not year % 10 == 0):
    print("Leap year not century year!")
else:
    print("Not leap nor century year!")

#Task Three: Time Traveler

today = date.today()
year_current = today.year

if(year < year_current):
    print(year, "is also a past year!")
elif(year > year_current):
    print(year, "is a future year!")
else:
    print(year, "is the current year!")

