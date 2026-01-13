class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = 0 

        while l < r:
            min_value = min(height[l], height[r])
            curr_area = (r - l) * min_value

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, curr_area) 

        return max_area


        