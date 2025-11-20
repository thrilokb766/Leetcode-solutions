class Solution(object):
    def mySqrt(self, x):
        if x<=1:
            return x
        low=0
        high=x//2
        while low<=high:
            mid=(low+high)//2
            sq=mid*mid
            if sq==x:
                return mid
            elif sq<x:
                low=mid+1
            else:
                high=mid-1
        return high

        