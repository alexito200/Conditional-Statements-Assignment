# Task 1 Identify the Greatest

first_number = int((input("Please provide your first number: ")))
second_number = int((input("Please provide your second number: ")))
third_number = int((input("Please provide your third number: ")))

def largest(first_number, second_number, third_number):
    if (first_number > second_number) and (first_number > third_number):
        largest_number = first_number
    elif (second_number > first_number) and (second_number > third_number):
        largest_number = second_number
    else:
        largest_number = third_number
    print("The largest number is: ", largest_number)

# Task 2 Identify the Smallest
def smallest(first_number, second_number, third_number):
    if (first_number < second_number) and (first_number < third_number):
        smallest_number = first_number
    elif (second_number < first_number) and (second_number < third_number):
        smallest_number = second_number
    else:
        smallest_number = third_number
    print("The smallest number is: ", smallest_number)

largest(first_number, second_number, third_number)
smallest(first_number, second_number, third_number)