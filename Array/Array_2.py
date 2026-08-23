arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

largest = arr[0]

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element =", largest)