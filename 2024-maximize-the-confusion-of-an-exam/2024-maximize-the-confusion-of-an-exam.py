class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        l=0
        ct=0
        cf=0
        ans=0
        for i in range(len(answerKey)):
            if answerKey[i]=="T":
                ct+=1
            else:
                cf+=1
            while(min(ct,cf)>k):
                if answerKey[l]=="T":
                    ct-=1
                else:
                    cf-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans
        