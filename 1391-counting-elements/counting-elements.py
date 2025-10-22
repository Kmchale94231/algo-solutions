class Solution(object):
    def countElements(self, arr):
        seen = set(arr)
        ans = 0
        
        for n in arr:
            num = n + 1
            if num in seen:
                ans +=1
        return ans
                
        
    
        
        