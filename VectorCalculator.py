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

#evaluate the total distance travelled by a particle given its velocity vector function (string), variable to integrate with respect to (string), lower limit (float), upper limit (float), output the total distance travelled (float)
def total_distance_travelled(vel_func_str, var_str, lower_limit, upper_limit):
    var = sympy.symbols(var_str)
    vel_func = sympy.sympify(vel_func_str)
    speed_func = sympy.sqrt(sum(comp**2 for comp in vel_func))
    total_distance = sympy.integrate(speed_func, (var, lower_limit, upper_limit))
    return float(total_distance)

def function_integral(expr_list, var_list, int_var): 
    variables = sympy.symbols(var_list)
    integrals = []
    for expr_str in expr_list:
        expr = sympy.sympify(expr_str)
        integral = sympy.integrate(expr, sympy.Symbol(int_var))
        integrals.append(integral) 
    return integrals

def function_definite_integral(expr_list, var_list, int_var, lower_limit, upper_limit):
    variables = sympy.symbols(var_list)
    definite_integrals = []
    for expr_str in expr_list:
        expr = sympy.sympify(expr_str)
        definite_integral = sympy.integrate(expr, (sympy.Symbol(int_var), lower_limit, upper_limit))
        definite_integrals.append(definite_integral.evalf())
    return definite_integrals 

#function to dot product two vectors
def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same length.")
    return sum(a * b for a, b in zip(vec1, vec2))

#function to find the angle between two vectors using dot product
def angle_between_vectors(vec1, vec2):
    dot_prod = dot_product(vec1, vec2)
    mag1 = vector_magnitude(vec1)
    mag2 = vector_magnitude(vec2)
    if mag1 == 0 or mag2 == 0:
        raise ValueError("Cannot compute angle with zero-length vector.")
    cos_theta = dot_prod / (mag1 * mag2)
    return math.acos(cos_theta)

#function to cross product two 3D vectors
def cross_product(vec1, vec2):
    if len(vec1) != 3 or len(vec2) != 3:
        raise ValueError("Both vectors must be 3-dimensional.")
    return [
        vec1[1]*vec2[2] - vec1[2]*vec2[1],
        vec1[2]*vec2[0] - vec1[0]*vec2[2],
        vec1[0]*vec2[1] - vec1[1]*vec2[0]
    ]

