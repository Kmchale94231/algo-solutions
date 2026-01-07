# Last updated: 1/7/2026, 9:25:33 AM
class Solution(object):
    def countElements(self, arr):
        seen = set(arr)
        ans = 0
        
        for n in arr:
            num = n + 1
            if num in seen:
                ans +=1
        return ans
                
        
    
        
        