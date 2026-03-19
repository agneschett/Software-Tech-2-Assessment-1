import time

# Basic example given
def sum_recursive(n):
    if n == 1:
        return 1
    return n + sum_recursive(n - 1)

def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Fibonacci
def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Factorial
def fact_recursive(n):
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)

def fact_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#test function
def test(func, n, repeat=10000):
    start = time.perf_counter()
    for _ in range(repeat):
        result = func(n)
    end = time.perf_counter()
    return result, (end - start) / repeat


#Running tests 
sizes = [5, 10, 20]

for n in sizes:
    print(f"\n=== n = {n} ===")

    print("Sum Recursive:", test(sum_recursive, n))
    print("Sum Iterative:", test(sum_iterative, n))

    print("Fib Recursive:", test(fib_recursive, n))
    print("Fib Iterative:", test(fib_iterative, n))

    print("Fact Recursive:", test(fact_recursive, n))
    print("Fact Iterative:", test(fact_iterative, n))