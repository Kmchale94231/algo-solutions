class Solution(object):
    def checkIfPangram(self, sentence):
        seen = set()
        
        for char in sentence:
            if char in seen:
                continue
            else:
                seen.add(char)
        total = len(seen)
        
        if total == 26:
            return True
        else:
            return False
        