class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            return str(x)[::-1] == str(x)
s = Solution()
result = s.isPalindrome(129)
print(result)