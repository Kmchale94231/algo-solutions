# Last updated: 1/27/2026, 3:49:44 PM
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        players = set()
        
        for w, l in matches:
            players.add(w)
            players.add(l)
            
            if l not in loses:
                loses[l] = 1
            else:
                loses[l] += 1
        
        zero = []
        one = []
        
        for p in players:
            if p not in loses:
                zero.append(p)
            elif loses[p] == 1:
                one.append(p)
        zero.sort()
        one.sort()
        
        return [zero, one]
                
            
            
            
        
        
        
        