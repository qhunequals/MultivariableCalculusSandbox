import math

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


# --- Test cases for VectorCalculator functions ---
if __name__ == "__main__":
    # Test vector_add_subtract
    print("Testing vector_add_subtract...")
    assert vector_add_subtract([1, 2], [3, 4], 'add') == [4, 6]
    assert vector_add_subtract([5, 7], [2, 3], 'sub') == [3, 4]

    # Test vector_magnitude
    print("Testing vector_magnitude...")
    assert abs(vector_magnitude([3, 4]) - 5.0) < 1e-9
    assert abs(vector_magnitude([0, 0, 0]) - 0.0) < 1e-9
    assert abs(vector_magnitude([1, 2, 2]) - 3.0) < 1e-9

    # Test scale_vector
    print("Testing scale_vector...")
    assert scale_vector([1, 2, 3], 2) == [2, 4, 6]
    assert scale_vector([0, -1], -3) == [0, 3]
    assert scale_vector([1, 0], 0) == [0, 0]

    # Test unit_vector
    print("Testing unit_vector...")
    assert unit_vector([3, 0]) == [1.0, 0.0]
    assert unit_vector([0, 4]) == [0.0, 1.0]
    try:
        unit_vector([0, 0, 0])
    except ValueError:
        print("Passed zero vector unit test.")
    result = unit_vector([1, 2, 2])
    expected = [1/3, 2/3, 2/3]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-9

    print("All tests passed!")


