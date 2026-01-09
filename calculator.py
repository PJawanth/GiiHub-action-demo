def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Sample calculations:")
    print("1 + 2 =", add(1, 2))
    print("5 - 3 =", subtract(5, 3))
    print("4 * 6 =", multiply(4, 6))
    print("10 / 2 =", divide(10, 2))
