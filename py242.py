class Solution(object):
    def isAnagram(self, s, t):   #anagram
        if len(s)!= len(t):
            return False
        else:
            return sorted(s) == sorted(t)
           
s = Solution()
print(s.isAnagram("anagram","nagaram"))