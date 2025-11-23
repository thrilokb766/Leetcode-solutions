class Solution(object):
    def totalFruit(self, fruits):
        left=0
        ans=0
        dici={}
        for m in range(len(fruits)):
            i=fruits[m]
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
            while len(dici)>2:
                l=fruits[left]
                dici[l]-=1
                if dici[l]==0:
                    dici.pop(l)
                left+=1
            ans=max(ans,m-left+1)
        return ans


