#Finding an Element in the Array Code
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

target = int(input("Enter element to search: "))

found = False

for i in range(n):
    if arr[i] == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")