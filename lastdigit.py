# Write a program to find the last digit of a number.
# The last digit can be found using the modulus operator (%).
num = int(input("Enter a number: "))
print("The last digit is:", num % 10)
print("_______________________________________________")

num = int(input("Enter a number: "))
last_digit = num % 10   # Calculate the last digit using modulus operator           
print(f"The last digit of {num} is {last_digit}.")
print("_______________________________________________")



num = int(input("Enter a number: "))
if num % 10 == 0:
    print("The last digit is 0.")
else:
    last_digit = num % 10
    print(f"The last digit of {num} is {last_digit}.")