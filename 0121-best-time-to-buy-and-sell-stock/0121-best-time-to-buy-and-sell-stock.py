class Solution(object):
    def maxProfit(self, prices):
        min1=prices[0]
        max1=0
        for i in range(1,len(prices)):
            if prices[i]<min1:
                min1=prices[i]         
            max1=abs(max(max1,prices[i]-min1))
        return max1
