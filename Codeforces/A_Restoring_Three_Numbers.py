# key: term 'ab' is equivalent to the mathematical operation of 'a + b'

nums = [int(x) for x in input().split()]
nums.sort()

print(nums[3] - nums[0], nums[3] - nums[1], nums[3] - nums[2])