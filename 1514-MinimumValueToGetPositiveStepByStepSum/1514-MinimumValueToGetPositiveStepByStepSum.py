# Last updated: 1/7/2026, 9:25:34 AM
class Solution(object):
    def minStartValue(self, nums):
        running_sum = 0
        lowest_point = 0
        start_value = 0
        
        for i in nums:
            running_sum += i
            if lowest_point > running_sum:
                lowest_point = running_sum
        
        start_value = 1 - lowest_point
        
        return start_value
        
            
        
        
        