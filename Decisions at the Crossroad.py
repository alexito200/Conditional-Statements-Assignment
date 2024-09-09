# Task 1 Code Correction

number = int(input("Enter a number: ")) # you have to add the int() function to convert user input from strings to integers

if number > 0:
    print("The number is positive.")
elif number == 0: # it's supposed to be ==, it was only =
    print("The number is zero.")
else: # I removed any code that came after else on this line
    print("The number is negative.")
