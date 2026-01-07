# Last updated: 1/7/2026, 9:25:39 AM
class Solution(object):
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        
        for num in range(n):
            if num in num_set:
                continue
            else: 
                return num
            
            
        
        
        
