#Write the program to accept percentage from the user and display the grade according to the following criteria:
# Percentage >= 90: Grade A
# Percentage >= 80 and < 90: Grade B
# Percentage >= 60 and < 80: Grade C
# Below : Grade D

percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    print("Grade A")
if percentage >= 80 and percentage < 90:
    print("Grade B")
if percentage >= 60 and percentage < 80:
    print("Grade C")
if percentage < 60:
    print("Grade D")