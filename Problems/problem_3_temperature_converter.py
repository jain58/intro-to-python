"""
Given a temperature in Fahrenheit, return the temperature in Celsius
"""

while True:
    # Ask for a temperature in Fahrenheit
    temp_F = input("Enter temp in F ")
    print("Temp in F " + str(temp_F))

    # C = (F-32)*5/9

    # Calculate it in Celsius
    temp_F = float(temp_F)
    temp_C = (temp_F-32)*5/9

    print("Temp in C "+str(temp_C))
    # Tell the user what it is
