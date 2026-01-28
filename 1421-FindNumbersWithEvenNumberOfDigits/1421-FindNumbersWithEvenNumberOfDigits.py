# Last updated: 1/28/2026, 5:39:48 PM
class Solution(object):
    def findNumbers(self, nums):
        count = 0
        
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count