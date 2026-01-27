# Last updated: 1/27/2026, 3:49:30 PM
1from collections import Counter
2
3class Solution:
4    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
5        n = len(nums)
6        counter = Counter(nums)
7        buckets = [0] * (n + 1)
8        
9        for num, freq in counter.items():
10            if buckets[freq] == 0:
11                buckets[freq] = [num]
12            else:
13                buckets[freq].append(num)
14        
15        ret = []
16        
17        for i in range(n, -1, -1):
18            if buckets[i] != 0:
19                ret.extend(buckets[i])
20            if len(ret) == k:
21                break
22            
23        return ret
24
25
26
27
28