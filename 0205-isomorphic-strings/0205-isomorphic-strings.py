class Solution(object):
    def isIsomorphic(self, s, t):
        dici={}
        seen=set()
        if len(s)!=len(t):
            return False
        for i,k in zip(s,t):
            if i in dici:
               if dici[i]!=k:
                return False
            else:
                if k in seen:
                    return False
                dici[i]=k
                seen.add(k)
        return True
