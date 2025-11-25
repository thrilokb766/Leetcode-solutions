class Solution(object):
    def lengthOfLongestSubstring(self, s):
        long=0
        left=0
        seen=set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[i])
            long=max(long,i-left+1)
        return long