# Get the phrase to repeat
x = input("Enter the phrase that you want me to repeat: ")

# Get the number of repetitions
num = int(input("How many times do you want me to repeat it: "))

# Repeat the phrase using a loop
for i in range(num + 1):  # Note: Python loops run from 0 to num (inclusive)
    print(x)
