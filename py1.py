class Solution(object):    #dicrionary approach, fast
    def twoSum(self, nums, target):
        h = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in h:
                return [i, h[complement]]
            h[nums[i]] = i
        return []

s = Solution()
print(s.twoSum([1,2,3,4],4))


class Solution(object):     #list approach, slow
    def twoSum(self, nums, target):
        list = []
        for i, num in enumerate(nums):
            if (target - num) not in list:
                list.append(num)
            else:
                return [list.index(target - num), i]

s = Solution()
print(s.twoSum([1,2,3,4],4))


class Solution(object):    #dicrionary approach, using enumerate
    def twoSum(self, nums, target):
        h = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in h:
                return [i, h[complement]]
            h[num] = i
        return []

s = Solution()
print(s.twoSum([1,2,3,4],4))