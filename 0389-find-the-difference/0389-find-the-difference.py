class Solution(object):
    def findTheDifference(self, s, t):
        if s=="":
            return t
        for  i in t:
            if t.count(i)>s.count(i) :
                return i
        