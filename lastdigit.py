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

print("_______________________________________________")

# Write a program to find the last digit of a entered by user is divided by 3 or not.
# The last digit can be found using the modulus operator (%).
# If the last digit is divisible by 3, print "Divisible by 3", otherwise print "Not divisible by 3".

num = int(input("Enter a number: "))
last_digit = num % 10
if last_digit % 3 == 0:
    print(f"The last digit {last_digit} of {num} is divisible by 3.")
else:
    print(f"The last digit {last_digit} of {num} is not divisible by 3.")