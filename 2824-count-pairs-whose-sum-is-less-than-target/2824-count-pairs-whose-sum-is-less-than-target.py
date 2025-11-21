class Solution(object):
    def countPairs(self, nums, target):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                subarray=nums[i]+nums[j]
                if subarray<target:
                    count+=1
        return count