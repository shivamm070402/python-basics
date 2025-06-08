# This code checks if a person is eligible to vote based on their age
age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("_______________________________________________")


# This code checks if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

print("_______________________________________________")

#Write a program to check whether a number is divisible by 7 or not
num = int(input("Enter a number: "))
if num % 7 == 0:
    print(f"{num} is divisible by 7.")
else:
    print(f"{num} is not divisible by 7.")
print("_______________________________________________")

#Write a program to display "Hello" if a number entered by user is a multiple of 5, otherwise display "Goodbye"
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Hello")
else:
    print("Goodbye")