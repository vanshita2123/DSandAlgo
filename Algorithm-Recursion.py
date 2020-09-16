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