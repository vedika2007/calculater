"""import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)

# Compute sine of x
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y, label='Sine Wave', color='blue', linestyle='--')

# Add labels and title
plt.xlabel('Angle [radians]')
plt.ylabel('sin(x)')
plt.title('Sine Wave using NumPy and Matplotlib')

# Add a legend
plt.legend()

# Show the grid
plt.grid(True)

# Display the plot
plt.show()"""

'''import numpy as np
import matplotlib.pyplot as plt

# Create an array of numbers from 1 to 10
x = np.arange(1, 11)

# Calculate squares of those numbers
y = np.square(x)

# Plot the graph
plt.plot(x, y, color='green', marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Number')
plt.ylabel('Square of Number')
plt.title('Square Numbers using NumPy and Matplotlib')

# Show the graph
plt.grid(True)
plt.show()'''

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



