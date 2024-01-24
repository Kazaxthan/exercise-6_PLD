#Exercise 6: Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those numbers which are divisible by 5

def divisible_by_5(numbers):
    divisible_numbers = [n for n in numbers if n % 5 == 0]
    return divisible_numbers

user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the user input into a list of integers
try:
    numbers = [int(x) for x in user_input.split()]
except ValueError:
    print("Invalid input. Please enter a valid list of numbers.")
    exit()

result = divisible_by_5(numbers)

print(f"Numbers divisible by 5 are: {result}")