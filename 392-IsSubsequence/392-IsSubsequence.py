# Last updated: 1/12/2026, 10:36:22 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        i = 0
4        j = 0
5
6        while i < len(s) and j < len(t):
7            if s[i] == t[j]:
8                i += 1
9            j += 1
10        
11        if i == len(s):
12            return True 
13        
14        else:
15            return False
16
17
18        