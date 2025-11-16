class Solution(object):
    def isPalindrome(self, s):
        c=""
        for i in s:
            if i.isalnum():
                c+=i.lower()
        if c==c[::-1]:
            return True 
        return False

            