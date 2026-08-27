# Program: Copy one array into another array

arr = []
copy_arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

# Copy each element
for i in range(n):
    copy_arr.append(arr[i])

print("Original array:", arr)
print("Copied array:", copy_arr)