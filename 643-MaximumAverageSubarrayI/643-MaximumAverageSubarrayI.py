# Last updated: 1/7/2026, 9:25:38 AM
class Solution(object):
    def findMaxAverage(self, nums, k):
	    curr = 0
	    for i in range(k):
	        curr += nums[i]
	    
	    ans = curr
	    
	    for i in range(k, len(nums)):
	        curr += nums[i] - nums[i - k]
	        ans = max(ans, curr)

	    return float(ans) / k
        
        
            
        
        
        
        
        
      
                
                
                
             
        
        

                
            
        
            
            
        
        
        