class Solution(object):
    def countSegments(self, s):
   
        segem = 0
        word = False

        for m in s:
            if m != " " and not word:
                segem += 1
                word = True
            elif m == " ":
                word = False

        return segem
