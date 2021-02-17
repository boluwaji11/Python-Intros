# This program assists a technician in the process
# of checking a substance's temperature.

# Named Constant to represent the maximum temperature
MAX_TEMP = 102.5

# Get the substance's temperature.
temperature = float(input("Enter the substance's Celsius temperature: "))

# As long as necessary, instruct the user to adjust the thermostat.
while temperature > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the termostat down and wait 5 minutes. \nThen take the temperature again and enter it')
    temperature = float(input("Enter the new Celsius temperature: "))

# Remind the user to check the temperature again in 15 minutes.
print('The temperature is acceptable.')
print('Check it again in 15 minutes.')
