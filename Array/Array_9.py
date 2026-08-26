# Program: Reverse an array

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

# Reverse the array
for i in range(n // 2):
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

print("Reversed array:", arr)