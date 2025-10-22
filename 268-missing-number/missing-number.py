class Solution(object):
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        
        for num in range(n):
            if num in num_set:
                continue
            else: 
                return num
            
            
        
        
        
