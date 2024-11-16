import numpy as np

def divided_diff(x_points, y_points):
    n = len(x_points)
   
    diff_table = np.zeros((n, n))
    
    diff_table[:, 0] = y_points
    
    
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i + 1][j - 1] - diff_table[i][j - 1]) / (x_points[i + j] - x_points[i])
    
    return diff_table

def newton_interpolation(x_points, y_points, x):
    
    diff_table = divided_diff(x_points, y_points)
    
    
    coefficients = diff_table[0, :]
    
    
    result = coefficients[0]
    n = len(x_points)
    
    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_points[j])
        result += term
    
    return result

def main():
    
    x_points = np.array([float(x) for x in input("Enter x-coordinates separated by space: ").split()])
    y_points = np.array([float(y) for y in input("Enter y-coordinates separated by space: ").split()])
    
    
    if len(x_points) != len(y_points):
        print("Error: The number of x and y coordinates must be the same.")
        return
    
   
    x = float(input("Enter the value of x to interpolate: "))
    
    
    interpolated_value = newton_interpolation(x_points, y_points, x)
    
   
    print(f"Interpolated value at x = {x}: {interpolated_value}")


if __name__ == "__main__":
    main()
