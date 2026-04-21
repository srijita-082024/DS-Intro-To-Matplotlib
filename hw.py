# Develop a choice based program where the user inputs the type of equation ( linear, quadratic and cubic (optional) ) and take the coefficients as input and plot the graph for them for range x = 0 to x = 50. 
import numpy as np
import matplotlib.pyplot as plt

def plot_linear(a, b):
    x = np.linspace(0, 50, 100)
    y = a * x + b
    plt.plot(x, y, label=f'Linear: y={a}x+{b}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Linear Equation Plot')
    plt.legend()
    plt.grid()
    plt.show()

def plot_quadratic(a, b, c):
    x = np.linspace(0, 50, 100)
    y = a * x**2 + b * x + c
    plt.plot(x, y, label=f'Quadratic: y={a}x^2+{b}x+{c}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Quadratic Equation Plot')
    plt.legend()
    plt.grid()
    plt.show()

def plot_cubic(a, b, c, d):
    x = np.linspace(0, 50, 100)
    y = a * x**3 + b * x**2 + c * x + d
    plt.plot(x, y, label=f'Cubic: y={a}x^3+{b}x^2+{c}x+{d}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Cubic Equation Plot')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    print("Choose the type of equation to plot:")
    print("1. Linear")
    print("2. Quadratic")
    print("3. Cubic (optional)")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        a = float(input("Enter coefficient a for linear equation (y = ax + b): "))
        b = float(input("Enter coefficient b for linear equation (y = ax + b): "))
        plot_linear(a, b)
        
    elif choice == 2:
        a = float(input("Enter coefficient a for quadratic equation (y = ax^2 + bx + c): "))
        b = float(input("Enter coefficient b for quadratic equation (y = ax^2 + bx + c): "))
        c = float(input("Enter coefficient c for quadratic equation (y = ax^2 + bx + c): "))
        plot_quadratic(a, b, c)
        
    elif choice == 3:
        a = float(input("Enter coefficient a for cubic equation (y = ax^3 + bx^2 + cx + d): "))
        b = float(input("Enter coefficient b for cubic equation (y = ax^3 + bx^2 + cx + d): "))
        c = float(input("Enter coefficient c for cubic equation (y = ax^3 + bx^2 + cx + d): "))
        d = float(input("Enter coefficient d for cubic equation (y = ax^3 + bx^2 + cx + d): "))
        plot_cubic(a, b, c, d)
        
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()