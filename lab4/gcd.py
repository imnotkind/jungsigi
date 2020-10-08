def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

if __name__ == "__main__":
    print(gcd_recursive(3, 5))
    print(gcd_recursive(3, 9))
    print(gcd_recursive(8, 12))
    print(gcd_recursive(12, 8))
    