class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        s=s.rstrip()
        for i in s[::-1]:
            if i not in  " ":
                count+=1
            else:
                break
        return count
        