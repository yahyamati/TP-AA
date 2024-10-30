

# def lagrange_polynomial_coefficients(x_points, y_points):
#     n = len(x_points)
#     coefficients = [0] * n  # Initialize a list for polynomial coefficients

#     for i in range(n):
#         # Start with [1.0] representing the constant term of L_i
#         term_coeffs = [1.0]

#         for j in range(n):
#             if i != j:
#                 # Multiply `term_coeffs` by (x - x_points[j]) / (x_points[i] - x_points[j])
#                 term_coeffs = multiply_polynomial_by_term(term_coeffs, -x_points[j], 1.0 / (x_points[i] - x_points[j]))

#         # Scale term coefficients by y_points[i] and add to overall polynomial
#         term_coeffs = [y_points[i] * coeff for coeff in term_coeffs]
#         coefficients = add_polynomials(coefficients, term_coeffs)

#     return coefficients[::-1]  # Reverse to have the highest degree first

# def multiply_polynomial_by_term(coeffs, constant_term, scale_factor):
#     # Multiply polynomial by (x - constant_term), scaled by `scale_factor`
#     result = [0] * (len(coeffs) + 1)
#     for i in range(len(coeffs)):
#         result[i] += -constant_term * coeffs[i] * scale_factor  # Multiply by constant term part
#         result[i + 1] += coeffs[i] * scale_factor  # Multiply by x part
#     return result

# def add_polynomials(poly1, poly2):
#     # Add two polynomials represented as lists of coefficients
#     len_diff = abs(len(poly1) - len(poly2))
#     if len(poly1) > len(poly2):
#         poly2 = [0] * len_diff + poly2
#     else:
#         poly1 = [0] * len_diff + poly1
#     return [a + b for a, b in zip(poly1, poly2)]

# def main():
#     # User inputs for x and y points
#     x_points = [float(x) for x in input("Enter x-coordinates separated by space: ").split()]
#     y_points = [float(y) for y in input("Enter y-coordinates separated by space: ").split()]
    
#     if len(x_points) != len(y_points):
#         print("Error: The number of x and y coordinates must be the same.")
#         return

#     # Calculate polynomial coefficients
#     coefficients = lagrange_polynomial_coefficients(x_points, y_points)
    
#     # Format the polynomial as a string, starting with the highest power
#     polynomial_str = "P(x) = " + " + ".join(f"{coef:.4f}x^{len(coefficients) - i - 1}" if len(coefficients) - i - 1 > 0 else f"{coef:.4f}" for i, coef in enumerate(coefficients) if coef != 0)
#     print(polynomial_str)

# if __name__ == "__main__":
#     main()



def lagrange_interpolation(x_points, y_points):
    n = len(x_points)
    coefficients = [0] * n  # Initialize the list for polynomial coefficients

    for i in range(n):
        # Start with a constant term for L_i
        term = [1]
        
        for j in range(n):
            if i != j:
                # Build each term in L_i using (x - x_points[j]) / (x_points[i] - x_points[j])
                term = multiply_term(term, -x_points[j], 1 / (x_points[i] - x_points[j]))

        # Scale the term by the corresponding y_points[i]
        term = [y_points[i] * coef for coef in term]
        
        # Add the term to the polynomial
        coefficients = add_polynomials(coefficients, term)
    
    return coefficients[::-1]  # Reverse to put the highest degree term first

def format_polynomial(coefficients):
    # Format the polynomial string from coefficients
    terms = []
    degree = len(coefficients) - 1
    for i, coef in enumerate(coefficients):
        if coef != 0:
            term = f"{coef:.4f}"
            if degree - i > 0:
                term += f"x^{degree - i}" if degree - i > 1 else "x"
            terms.append(term)
    return "P(x) = " + " + ".join(terms)

def multiply_term(coeffs, constant, scale):
    # Helper to multiply polynomial by (x - constant) with a scale factor
    result = [0] * (len(coeffs) + 1)
    for i, coef in enumerate(coeffs):
        result[i] += -constant * coef * scale
        result[i + 1] += coef * scale
    return result

def add_polynomials(poly1, poly2):
    # Helper to add two polynomials represented by lists of coefficients
    if len(poly1) < len(poly2):
        poly1 = [0] * (len(poly2) - len(poly1)) + poly1
    elif len(poly2) < len(poly1):
        poly2 = [0] * (len(poly1) - len(poly2)) + poly2
    return [a + b for a, b in zip(poly1, poly2)]

# Example usage
x_points = [float(x) for x in input("Enter x-coordinates separated by space: ").split()]
y_points = [float(y) for y in input("Enter y-coordinates separated by space: ").split()]

if len(x_points) == len(y_points):
    coefficients = lagrange_interpolation(x_points, y_points)
    polynomial = format_polynomial(coefficients)
    print(polynomial)
else:
    print("Error: x and y coordinates must have the same number of points.")

