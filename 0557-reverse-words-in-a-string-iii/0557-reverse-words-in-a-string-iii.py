class Solution(object):
    def reverseWords(self, s):
        res=[]
        words=s.split()
        for i in words:
            rev=""
            for j in i:
                rev=j+rev
            res.append(rev)
        return " ".join(res)
