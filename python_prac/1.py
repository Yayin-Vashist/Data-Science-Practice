def fourSum(nums, target):
    nums.sort()
    ans = []
    for i in range(len(nums)):
        for j in range(len(nums) - 1, -1, -1):
            temp = target - nums[i] - nums[j]
            s = i + 1
            f = j - 1
            while s < f:
                if nums[s] == nums[s - 1] or nums[f] == nums[f + 1]:
                    while nums[s] == nums[s - 1]:
                        s += 1
                        while nums[f] == nums[f + 1]:
                            f -= 1
                    if nums[s] + nums[f] == temp:
                        ans.append([nums[i], nums[j], nums[s], nums[f]])
                    elif nums[s] + nums[f] >= temp:
                        s += 1
                    elif nums[s] + nums[f] <= temp:
                        f -= 1
    return ans


fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)
