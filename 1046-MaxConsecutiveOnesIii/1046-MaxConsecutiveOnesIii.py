# Last updated: 1/7/2026, 9:25:36 AM
class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        zeros = 0
        curr = 0
        ans = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
                
            while zeros > k:
                if nums[l] == 0:
                    l += 1
                    zeros -= 1
                else:
                    l += 1
                        
            curr = r - l + 1
            ans = max(ans, curr)
        return ans
            
        
                        
                    
                
                
        
        

                    
            
            
                
                    
        
       
            
            

                
            
                    
                    
        
        
        
        