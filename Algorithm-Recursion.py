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

# Reversing a string by using recursion
def reverse(word):
    size = len(word)
    if size == 0:
        return
    last_char = word[size-1]
    print(last_char, end='')
    return reverse(word[0:size-1])

reverse("hello world")



def nextHappy(N):
    i = 0
    sum = 0
    p = N + 1
    k = p
    if p < 10:
        p = 10
    while (p % 10 != 0):
        r = p % 10
        sum = sum + r ** 2
        p = p // 10
    if (sum == 1):
        return k

    return nextHappy(N + 1)


print(nextHappy(8))