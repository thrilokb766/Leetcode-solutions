class Solution(object):
    def findDuplicates(self, nums):
        dici={}
        res=[]
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        for i,k in dici.items():
            if k>1:
                res.append(i)
        return res
        