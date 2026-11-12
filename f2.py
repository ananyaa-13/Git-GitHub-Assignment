a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
elif choice == 5:
    if b != 0:
        print("Result:", a % b)
    else:
        print("Cannot calculate modulus by zero")
elif choice == 6:
    print("Result:", a ** b)
else:
    print("Invalid Choice")