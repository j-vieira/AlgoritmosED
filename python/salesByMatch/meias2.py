n = 7
arr = [1, 2, 1, 2, 1, 3, 2]
par = 0

for value in arr:
    par += arr.count(value) % 2
    arr = [item for item in arr if item != value]
    #print(arr.count(value))
    print(arr)