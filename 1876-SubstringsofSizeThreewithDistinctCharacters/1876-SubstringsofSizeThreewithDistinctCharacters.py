# Last updated: 1/21/2026, 12:52:52 AM
1class Solution:
2    def countGoodSubstrings(self, s: str) -> int:
3        count = 0
4        
5        for i in range(len(s) - 2):
6            if len(set(s[i:i+3])) == 3:
7                count += 1
8        return count
9
10