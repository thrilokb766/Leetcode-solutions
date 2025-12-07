class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)//2
        dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        for j ,k in dici.items():
            if k>n:
                return j

        