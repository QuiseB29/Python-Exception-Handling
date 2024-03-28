def safe_divide(b,a):
    try:
        return b / a
    except ZeroDivisionError:
        return "Division by zero is not allowed"
while True:
    try:
        a = float(input("Enter the orginal amount of serving?"))
        b = int(input("Enter the future amount of serving?"))
        result = safe_divide(b,a)
        print(f"Adjustment factor {result}")
    except ValueError:
        print("That's not a number try again")
    finally:
        print("Thank you for using serving calculater.")