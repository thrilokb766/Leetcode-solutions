class Solution(object):
    def lengthOfLongestSubstring(self, s):
        num=set()
        ans=0
        l=0
        for i in range(len(s)):
            ch=s[i]
            if ch not in num:
                num.add(ch)
            else:
                while ch in num:
                    num.remove(s[l])
                    l+=1
                num.add(ch)
            ans=max(ans,i-l+1)
        return ans