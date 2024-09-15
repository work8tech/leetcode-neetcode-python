class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # Take the first string as the reference
        prefix = strs[0]
        # Compare the prefix with each string in the array
        for s in strs[1:]:
            while s[:len(prefix)] != prefix and prefix:
            # Reduce the prefix by one character at a time
                prefix = prefix[:len(prefix)-1]
        return prefix

s = Solution()
print(s.longestCommonPrefix(['superman', 'superdog', 'superhero', 'supper']))