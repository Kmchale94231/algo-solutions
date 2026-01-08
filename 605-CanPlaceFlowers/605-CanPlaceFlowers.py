# Last updated: 1/8/2026, 12:08:46 PM
1class Solution(object):
2    def reverseVowels(self, s):
3        vowels = "aeiouAEIOU"
4        string = list(s)
5        l, r = 0, len(string) - 1 
6
7        while l < r:
8            if string[l] in vowels and string[r] in vowels:
9                string[l], string[r] = string[r], string[l]
10                l += 1
11                r -= 1
12            elif string[l] not in vowels:
13                l += 1
14            elif string[r] not in vowels:
15                r -= 1
16        return "".join(string) 
17            
18
19
20            
21
22            
23        