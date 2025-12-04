class Solution(object):
    def backspaceCompare(self, s, t):
        def build(string):
            stack = []   
            
            for ch in string:
                if ch != '#':
                     
                    stack.append(ch)
                else:
                    
                    if stack:
                        stack.pop()
            
           
            return "".join(stack)
        
        
        return build(s) == build(t)
