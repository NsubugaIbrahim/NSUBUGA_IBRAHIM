def division(x, y):
    return x/y
def main():
    while True:
        print("\n--- Division Program ---")
        print("Enter two numbers to find their quotient. (x/y)")
        x = float(input("Enter the first number x: "))
        y = float(input("Enter the second numbery: "))
        try:
            result = division(x, y)
            print(f"The quotient of {x} and {y} is {result}")
            break # Exit the loop if division is successful
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Please enter valid numbers.")
if __name__ == "__main__":
    main()
    