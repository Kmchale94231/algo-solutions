# Last updated: 1/7/2026, 9:25:39 AM
class Solution(object):
    def reverseString(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        

            
            
        
        
        
            