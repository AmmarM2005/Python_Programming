#Sum and Average
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

total = 0

for i in range(n):
    total = total + arr[i]

average = total / n

print("Sum =", total)
print("Average =", average)