import VectorCalculator as vcalc
import math
import sympy



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


# run the tests
if __name__ == "__main__":
    test_differentiate_function()
    test_integrate_function()
    test_definite_integral()
    test_evaluate_expression()