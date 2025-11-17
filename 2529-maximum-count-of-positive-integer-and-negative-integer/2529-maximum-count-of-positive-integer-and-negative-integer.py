class Solution(object):
    def maximumCount(self, nums):
        negcount=0
        poscount=0
        for i in range(len(nums)):
            if nums[i]<0:
                negcount+=1
            elif nums[i]>0:
                poscount+=1
        return max(negcount,poscount)
            