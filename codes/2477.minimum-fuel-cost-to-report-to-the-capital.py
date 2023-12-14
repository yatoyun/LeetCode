#
# @lc app=leetcode id=2477 lang=python3
#
# [2477] Minimum Fuel Cost to Report to the Capital
#

from collections import defaultdict
# @lc code=start
class Solution:
    def __init__(self):
        self.paths = defaultdict(list)
        self.seats = None
        self.fuel = 0
        
    def dfs(self, ex, current):
        if len(self.paths[current]) == 1 and self.paths[current] == ex:
            self.fuel += 1
            return 1
        
        num_rep = 1
        for path in self.paths[current]:
            if path == ex:
                continue
            num_rep += self.dfs(current, path)
        
        if ex == None:
            return num_rep - 1
        
        self.fuel += num_rep // self.seats + bool(num_rep % self.seats)
        return num_rep
            
        
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:  
        self.seats = seats
        for n1, n2 in roads:
            self.paths[n1].append(n2)
            self.paths[n2].append(n1)
        
        self.dfs(None, 0)
        return self.fuel
        
        
# @lc code=end

