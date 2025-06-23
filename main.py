#WE ARE CREATING A COMPOUND INTEREST CALCULATOR
#P = principle
#R = Rate
#T = Time
#N = Numbers of years 
#A = Amount
import math
principal = 0
rate = 0
time = 0

while principal  <= 0:
        principal = float(input(f"Enter the principle amount: \n"))
        if principal <= 0:
         print("principle can't be less than or equal to zero")
        else:
         break

while rate <= 0:
    rate = float(input("Enter the interest rate: \n"))
if rate <= 0:
        print("Interest can't be less than or equal to zero: \n")

while time <= 0:
   time = float(input("Enter the time in years: \n"))
if time <= 0:
        print("Time can't be less than or equal to zero: \n")

total = principal * pow((1 + rate / 100),time)
print(f"Your balance after {time} years/s: ${total:.2f}")

