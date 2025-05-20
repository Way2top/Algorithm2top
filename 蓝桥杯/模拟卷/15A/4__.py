# 回文数组

n = int(input())
nums = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    if nums[left] == nums[right]:
        left += 1
        right -= 1
    else:
        if (nums[left] - nums[right]) * (nums[left + 1] - nums[right - 1]) > 0:
            nums