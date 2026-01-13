# Last updated: 1/12/2026, 10:21:00 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        l = 0
4        r = 0
5
6
7        while r < len(nums): 
8            if nums[r] != 0:
9                nums[l], nums[r] = nums[r], nums[l]
10                l += 1 
11                r += 1
12            else:
13                r += 1
14        return nums     