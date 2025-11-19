class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low=0
        high=len(letters)-1
        while low<=high:
            mid=(low+high)//2
            if target<letters[mid]:
                high=mid-1
            else:
                low=mid+1
        return letters[low % len(letters)]