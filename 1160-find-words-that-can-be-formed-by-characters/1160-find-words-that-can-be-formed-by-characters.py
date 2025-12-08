class Solution(object):
    def countCharacters(self, words, chars):
      
        freq = {}
        for c in chars:
            freq[c] = freq.get(c, 0) + 1
        
        total = 0
        for word in words:
            temp = {}
            valid = True
            for c in word:
                temp[c] = temp.get(c, 0) + 1
                if temp[c] > freq.get(c, 0):
                    valid = False
                    break
            
            if valid:
                total += len(word)
        
        return total
