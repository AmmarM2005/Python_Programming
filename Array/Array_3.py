arr = [40, 10, 50, 20, 30]

smallest = arr[0]

for i in range(1, len(arr)):

    if arr[i] < smallest:
        smallest = arr[i]

print("Smallest element =", smallest)