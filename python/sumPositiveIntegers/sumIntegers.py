def sum_integers(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result


print(sum_integers(1000000000000000))
