class Solution(object):
    def wordPattern(self, pattern, s):
        words=s.split()
        dici={}
        seen=set()
        if len(pattern)!=len(words):
            return False
        for i,j in zip(pattern,words):
            if i in dici:
                if dici[i]!=j:
                    return False
            else:
                if j in seen:
                    return False
                dici[i]=j
                seen.add(j)
        return True