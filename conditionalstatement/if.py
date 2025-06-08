
# This code checks if a number is greater than 15 and prints a message if true.
i = 10

 # Checking if i is greater than 15
if (i > 15):
    print("10 is less than 15")
    
print("I am Not in if")

print("_______________________________________________")

# This code checks if a number is greater than 18 and prints a message if true.

age = 19
if age > 18: print("Eligible to Vote.")

age = int(input("Enter your age: "))
if age > 18:
     print("Eligible to Vote.",age)

print("_______________________________________________")

# Write a program to calculate the electricity bill based on the number of units consumed.
#units                      price
#First 100 units          No change
#Next 100 units           Rs 5 per unit
#After 200 units          Rs 10 per unit

amt = 0
units = int(input("Enter the number of units consumed: "))
if units < 100:
    amt = 0
if units >= 100 and units < 200:
    amt = (units - 100) * 5
if units >= 200:
    amt = (100 * 5) + ((units - 200) * 10)
print(f"Electricity bill for {units} units is Rs {amt}")

print("_______________________________________________")