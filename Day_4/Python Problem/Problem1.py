"""You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 

Example 1:

Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.
"""

class Solution(object):
    def maxDistance(self, s, k):
        ans = 0
        north = south = east = west = 0
        for it in s:
            if it == "N":
                north += 1
            elif it == "S":
                south += 1
            elif it == "E":
                east += 1
            elif it == "W":
                west += 1
            t1 = min(north, south, k)
            t2 = min(east, west, k - t1)
            ans = max(ans,self.count(north, south, t1) + self.count(east, west, t2))
        return ans

    def count(self, drt1, drt2, times):
        return abs(drt1 - drt2) + times * 2
    

sol = Solution()

print(sol.maxDistance("NSEW", 0))  
print(sol.maxDistance("NWSE", 1))  
print(sol.maxDistance("NSWWEW", 1))  
print(sol.maxDistance("NNNN", 2))  
print(sol.maxDistance("NSNSNSNS", 4))  
print(sol.maxDistance("", 5))  
print(sol.maxDistance("E", 0))  
