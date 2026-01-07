# Last updated: 1/7/2026, 9:25:29 AM
class Solution(object):
    def getAverages(self, nums, k):
        l = 0
        ans = [-1] * len(nums)
        window_size = k*2 + 1
        total = 0 
        
        
        for right, value in enumerate(nums):
            total += value
            
            if right - l + 1 == window_size:
                ans[l + k] = total // window_size
                
                total -= nums[l]
                l += 1
                
        return ans
                
            
        
            
            
            
            
            
            
            
            
        
        
        
        
        