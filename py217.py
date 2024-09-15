class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)!= len(set(nums))
        
s= Solution()
result = s.containsDuplicate([1,2,3])
print(result)