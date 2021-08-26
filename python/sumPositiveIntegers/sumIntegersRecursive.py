def sumIntegersRecursive(n):
    if n == 0:
        return 0
    else:
        return n + sumIntegersRecursive(n - 1)


print(sumIntegersRecursive(100))
