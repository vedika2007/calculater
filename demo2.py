

import numpy as np
import matplotlib.pyplot as plt

print("Welcome to the NumPy Calculator with Graph!")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")

# Get user choice
choice = int(input("Enter your choice (1-5): "))

# Input two numbers (or ranges)
x = np.linspace(1, 10, 10)
y = float(input("Enter a number: "))

# Perform operation
if choice == 1:
    result = x + y
    operation = "Addition"
elif choice == 2:
    result = x - y
    operation = "Subtraction"
elif choice == 3:
    result = x * y
    operation = "Multiplication"
elif choice == 4:
    result = x / y
    operation = "Division"
elif choice == 5:
    result = x ** y
    operation = "Power"
else:
    print("Invalid choice.")
    exit()

# Print result
print(f"\nInput range: {x}")
print(f"Result of {operation} with {y}:")
print(result)

# Plot the result
plt.plot(x, result, marker='o')
plt.title(f'{operation} Result')
plt.xlabel('x values (1 to 10)')
plt.ylabel('Result')
plt.grid(True)
plt.show()




