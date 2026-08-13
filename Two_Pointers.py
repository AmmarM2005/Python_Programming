a = [1, 2, 4, 6, 8, 9, 11]
n = 7
target = 10

left = 0
right = n - 1

while left < right:
    sum = a[left] + a[right]

    if sum == target:
        print(f"Found: {a[left]} + {a[right]} = {target}")
        break

    elif sum < target:
        left += 1

    else:
        right -= 1

else:
    print("No pair found")