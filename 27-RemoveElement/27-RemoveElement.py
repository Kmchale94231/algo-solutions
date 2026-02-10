# Last updated: 2/9/2026, 11:56:22 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        count = 0 


        while l <= r:
            
            if nums[l] != val:
                l += 1

            elif nums[r] == val:
                r -= 1

            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        for i in range(len(nums)):
            if nums[i] == val:
                break
            count += 1
        
                
        return count

            
            