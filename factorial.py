def factorial(number):
   if number == 0 or number == 1:
       return 1
   else:
       return number * factorial(number-1)

    
def main():
    number = int(input("Enter a number of your choice to calculate its factorial: "))
    try:
        if number < 0:
            print("Factorial is not defined for negative numbers")
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
    except ValueError:
        print("Please enter a valid integer")
if __name__ == "__main__":
    main()