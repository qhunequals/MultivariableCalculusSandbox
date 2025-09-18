import math
import sympy 

def vector_add_subtract(vec1, vec2, operation):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same length.")
    if operation == 'add':
        return [a + b for a, b in zip(vec1, vec2)]
    elif operation == 'sub':
        return [a - b for a, b in zip(vec1, vec2)]
    else:
        raise ValueError("Operation must be 'add' or 'sub'.")

def vector_magnitude(vector):
    return math.sqrt(sum(x**2 for x in vector))


def scale_vector(vector, scalar):
    return [scalar * x for x in vector]

def unit_vector(vector):
    mag = vector_magnitude(vector)
    if mag == 0:
        raise ValueError("Zero vector has no direction (undefined unit vector).")
    return [x / mag for x in vector]



# given input function (string), variable to differentiate with respect to (string), output the derivative with respect to that variable (string)
def differentiate_function(func_str, var_str):
    var = sympy.symbols(var_str)
    func = sympy.sympify(func_str)
    derivative = sympy.diff(func, var)
    return str(derivative)

#given input function (string), variable to antidifferentiate with respect to (string), output the integral with respect to that variable (string)
def integrate_function(func_str, var_str):
    var = sympy.symbols(var_str)
    func = sympy.sympify(func_str)
    integral = sympy.integrate(func, var)
    return str(integral)

#evaluate a definite integral given input function (string), variable to integrate with respect to (string), lower limit (float), upper limit (float), output the definite integral (float)
def definite_integral(func_str, var_str, lower_limit, upper_limit):
    var = sympy.symbols(var_str)
    func = sympy.sympify(func_str)
    integral = sympy.integrate(func, (var, lower_limit, upper_limit))
    return float(integral)

#evaluate an expression at a value given input expression (string), variable to evaluate (string), value to evaluate at (float), output the evaluated expression (float)
def evaluate_expression(expr_str, var_str, value):
    var = sympy.symbols(var_str)
    expr = sympy.sympify(expr_str)
    evaluated = expr.subs(var, value)
    return float(evaluated)

