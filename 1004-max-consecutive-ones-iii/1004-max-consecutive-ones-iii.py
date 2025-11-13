class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        temp=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==0:
                temp+=1
            while temp>k:
                if nums[l]==0:
                    temp-=1
                l+=1
            maxi=max(maxi,i-l+1)
        return maxi
