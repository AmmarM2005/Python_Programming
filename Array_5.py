#Program to count the frequency of an element using Array
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

target = int(input("Enter element to count: "))

count = 0

for i in range(n):
    if arr[i] == target:
        count = count + 1

print(target, "occurs", count, "times")