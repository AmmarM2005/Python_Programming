#Basic Array Code for DSA
nums = [10, 20, 30, 40, 50]
print(nums[2]) 
nums.append(60)
target = 40
found = False
for x in nums:
    if x == target:
        found = True
        break
print(found)