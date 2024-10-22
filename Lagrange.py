import numpy as np
import matplotlib.pyplot as plt

def lagrange_function(x_points, y_points, x):
    
    n = len(x_points)
    P = 0
    
    

    for i in range(n):
        
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        
        
        P += y_points[i] * L_i

    return P

def main():
    
    x_points = np.array([float(x) for x in input("Enter x-coordinates separated by space: ").split()])
    y_points = np.array([float(y) for y in input("Enter y-coordinates separated by space: ").split()])
    
    if len(x_points) != len(y_points):
        print("Error: The number of x and y coordinates must be the same.")
        return

   
    x_value = float(input("Enter the x value to calculate: "))
    
    
    lagrange_value = lagrange_function(x_points, y_points, x_value)
    
   
    print(f"Interpolated value at x = {x_value}: P({x_value}) = {lagrange_value}")
    
    
    

if __name__ == "__main__":
    main()
