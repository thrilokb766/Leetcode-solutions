class Solution(object):
    def findLengthOfLCIS(self, nums):
       
        count=1
        max1=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
                max1=max(max1,count);
            else:
                count=1
        return max1