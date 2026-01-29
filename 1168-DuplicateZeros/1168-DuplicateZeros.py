# Last updated: 1/28/2026, 11:33:04 PM
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        num_zeros = 0

        for num in arr:
            if num == 0:
                num_zeros += 1

        j = len(arr) - 1 + num_zeros
        i = len(arr) - 1

        while i != j:
            if j < len(arr):
                arr[j] = arr[i]
            j -= 1

            if arr[i] == 0:
                if j < len(arr):
                    arr[j] = arr[i] 
                j -= 1
            i -= 1

            
        
        