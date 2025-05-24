def division(x, y):
    return x/y
def main():
    print("Enter two numbers to find their quotient. (x/y)")
    x = float(input("Enter the first number x: "))
    y = float(input("Enter the second numbery: "))
    result = division(x, y)
    print(f"The quotient of {x} and {y} is {result}")
if __name__ == "__main__":
    main()