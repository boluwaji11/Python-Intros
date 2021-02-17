# This program uses a loop to display a
# table of numbers and their squares

# Get the ending limit.
print('This program displays a list of numbers and their squares.')
start = int(input("What is your starting number? "))
end = int(input('How high should I go? '))

# Print the table headings.
print()
print('Number\tSquare')
print('--------------')

# Print the numbers and their squares.
for number in range(start,end + 1):
    square = number**2
    print(number, '\t', square)
