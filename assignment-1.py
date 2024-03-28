def temperature(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5/9
        print('%0.2f Fahrenheit is equivalent to %.2f Celsius' % (fahrenheit, celsius))
    except ZeroDivisionError:
        return "Cannot provide degree at 0"

while True:
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f'{fahrenheit} degrees Fahrenheit')
        temperature(fahrenheit)
    except ValueError:
        print("Oops, that's not a valid number.")
    finally:
        print("Have a good day and Thank you for using the weather app")
