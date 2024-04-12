MAX_TEMP = 102.5

temperature=float(input("Enter the substance's celsius temperature: "))

while temperature > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 Minutes. Then take the temperature')
    print('again and enter it')
    temperature=float(input('Enter the new celsius temperature: '))

print('The temperature is acceptable.')
print('Check it again in 15 minutes.')
