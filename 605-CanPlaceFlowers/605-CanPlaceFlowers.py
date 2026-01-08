# Last updated: 1/8/2026, 11:51:39 AM
1class Solution(object):
2    def canPlaceFlowers(self, flowerbed, n):
3        array = [0] + flowerbed + [0]
4        i = 1
5        
6        while i < len(array) - 1:
7            if array[i - 1] == 0 and array[i] == 0 and array[i + 1] == 0:
8                array[i] = 1
9                n -= 1
10                i += 2
11            else:
12                i += 1
13        
14        if n <= 0:
15            return True 
16        
17        return n <= 0