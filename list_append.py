# This prigram demonstrates how the append method
# can be used to add items to a list

def main():
    # First, create an empty list
    name_list = []

    # Create a variable to control the list
    again = 'y'

    # Add some names to the list.
    while again == 'y':
        # Get a name from the user.
        name = input('Enter a name: ')

        # Append the name to the list.
        name_list.append(name)

        # Add another one?
        print('Do you want to add another name?')
        again = input('y = yes, anything else = No: ')
        print()
    
    # Display the names that were created.
    print('Here are the names you entered.')

    for name in name_list:
        print(name)

# Call the main function
main()