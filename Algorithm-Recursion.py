# Factorial of a number
# Iterative
def fact(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result

# Recursive

def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

print(fact(4))
print(factorial(5))

# Fibonacci
# Iterative approach
def fibonacci_iterative(num):
    a = 0
    b = 1
    sum = 0
    for i in range(num):
        sum = a+b
        a = b
        b = sum
    return sum

# Recursive approach
def fibonacci_recursive(num):
    if num < 2:
        return num
    return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)

print(fibonacci_recursive(4))
print(fibonacci_iterative(4))