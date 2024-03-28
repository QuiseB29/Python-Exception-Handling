# Python Program to convert temperature in fahrenheit to celsius

while True:
    try:
        # User input for temperature in Fahrenheit
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        # calculate celsius
        celsius = (fahrenheit - 32) / 1.8

        print ('%0.2f Fahrenheit is equivalent to: %.2f Celsius' % (fahrenheit ,celsius))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    finally:
        print("Thank you for using the weather forecast application!")
