def factorial_sequential(n):    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


if __name__ == "__main__":
    for i in range(10):
        print(factorial_sequential(i), factorial_recursive(i))