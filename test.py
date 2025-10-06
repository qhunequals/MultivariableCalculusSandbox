import VectorCalculator as vcalc
import math
import sympy


#test the vector_add_subtract function with addition
def test_vector_add_subtract_add():
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    expected = [5, 7, 9]
    result = vcalc.vector_add_subtract(vec1, vec2, 'add')
    print("Result:", result)
    print("Expected:", expected, "\n")


#test the vector_add_subtract function with subtraction
def test_vector_add_subtract_sub():
    vec1 = [4, 5, 6]
    vec2 = [1, 2, 3]
    expected = [3, 3, 3]
    result = vcalc.vector_add_subtract(vec1, vec2, 'sub')
    print("Result:", result)
    print("Expected:", expected, "\n")


# test the vector_magnitude function
def test_vector_magnitude():
    vec = [3, 4]
    expected = 5.0
    result = vcalc.vector_magnitude(vec)
    print("Result:", result)
    print("Expected:", expected, "\n")


# test the scale_vector function
def test_scale_vector():
    vec = [1, 2, 3]
    scalar = 2
    expected = [2, 4, 6]
    result = vcalc.scale_vector(vec, scalar)
    print("Result:", result)
    print("Expected:", expected, "\n")


# test the unit_vector function
def test_unit_vector():
    vec = [3, 4]
    expected = [0.6, 0.8]
    result = vcalc.unit_vector(vec)
    print("Result:", result)
    print("Expected:", expected, "\n")


# test the differentiate_function function with a simple polynomial
def test_differentiate_function():
    func_str = "x**2 + 3*x + 2"
    var_str = "x"
    expected = "2*x + 3"
    result = vcalc.differentiate_function(func_str, var_str)
    print("Result:", result)
    print("Expected:", expected, "\n")
 


# test the integrate_function function with a simple polynomial
def test_integrate_function():
    func_str = "2*x + 3"
    var_str = "x"
    expected = "x**2 + 3*x"
    result = vcalc.integrate_function(func_str, var_str)
    print("Result:", result)
    print("Expected:", expected, "\n")


# test the definite_integral function with a simple polynomial and limits
def test_definite_integral():
    func_str = "2*x"
    var_str = "x"
    lower_limit = 0
    upper_limit = 2
    expected = 4.0
    result = vcalc.definite_integral(func_str, var_str, lower_limit, upper_limit)
    print("Result:", result)
    print("Expected:", expected, "\n")


# test the evaluate_expression function with a simple polynomial and value
def test_evaluate_expression():
    expr_str = "x**2 + 3*x + 2"
    var_str = "x"
    value = 2
    expected = 12.0
    result = vcalc.evaluate_expression(expr_str, var_str, value)
    print("Result:", result)
    print("Expected:", expected, "\n")

# test the total_distance_travelled function with a velocity parametric function
def test_total_distance_travelled():
    velocity_func_str = "3*t**2 - 2*t + 1"
    var_str = "t"
    lower_limit = 0
    upper_limit = 2
    # The expected value is the integral of the absolute value of the velocity function from 0 to 2
    expected = 10.666666666666666
    result = vcalc.total_distance_travelled(velocity_func_str, var_str, lower_limit, upper_limit)
    print("Result:", result)
    print("Expected:", expected, "\n")


# run the tests
if __name__ == "__main__":
    test_vector_add_subtract_add()
    test_vector_add_subtract_sub()
    test_vector_magnitude()
    test_scale_vector()
    test_unit_vector()
    test_differentiate_function()
    test_integrate_function()
    test_definite_integral()
    test_evaluate_expression()

    # unit vector of a vector (2, -1, -2)
    vec = [2, -1, 2]
    unit_vec = vcalc.unit_vector(vec)
    print("Unit vector of", vec, "is", unit_vec)