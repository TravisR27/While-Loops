# This task will show how the user is repeatedly asked to enter a number and when the user inputs a wrong value the program will break.

# This shows the infinite list of the amount of numbers a user can enter.
nums = []

# Initialize a variable to store the user input
user_input = 0

# Use a while loop to keep asking the user for a number
while user_input != -1:

# Try to convert the user input to an integer
  try:
    user_input = int(input("Enter a number: "))

# If the user input is not -1, append it to the list
    if user_input != -1:
      nums.append(user_input)

# If the user input is not a valid integer, print an error message
  except ValueError:
    print("Invalid input. Please enter an integer.")

# Sum of all numbers added together to get your average
avg = sum(nums)/(len(nums))

# Output of all numbers entered and put into a average
print(f"The sum of the numbers you entered is {avg}.")