nums = [3, 7, 1, 9, 2, 8, 5]
for num in nums:
  if num % 2 == 0:
    print(num)

for num in nums:
  if num > 5:
    print(num)

doubled_nums = [num + num for num in nums]
print([doubled_num for doubled_num in doubled_nums])

nums.sort()
print([num for num in nums])

nums.reverse()
print(nums)
