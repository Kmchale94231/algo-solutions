# Last updated: 1/28/2026, 11:27:04 PM
1class Solution:
2    def duplicateZeros(self, arr: List[int]) -> None:
3        num_zeros = 0
4
5        for num in arr:
6            if num == 0:
7                num_zeros += 1
8
9        j = len(arr) - 1 + num_zeros
10        i = len(arr) - 1
11
12        while i != j:
13            if j < len(arr):
14                arr[j] = arr[i]
15            j -= 1
16
17            if arr[i] == 0:
18                if j < len(arr):
19                    arr[j] = arr[i] 
20                j -= 1
21            i -= 1
22
23            
24        
25        