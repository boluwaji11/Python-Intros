# This program display the conversion of KPH to MPH

# Named constant for conversion
KPH_TO_MPH = 0.6214

# Display Headers
print('KPH\tMPH')
print('--------------')

# The for loop iterations
for kph_speed in range(60,131,10):
    mph_speed = kph_speed * KPH_TO_MPH
    print(kph_speed, '\t', format(mph_speed,'.1f'))
