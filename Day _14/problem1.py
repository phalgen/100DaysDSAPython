"""You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

Return the minimum possible sum of the area of these rectangles.

Note that the rectangles are allowed to touch.

 

Example 1:

Input: grid = [[1,0,1],[1,1,1]]

Output: 5

Explanation:



The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
The 1 at (1, 1) is covered by a rectangle of area 1."""




class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        def area(a, b, c, d):
            lx, ly, ty, dy = cols, 0, rows, 0
            for i in range(a, b + 1):
                for j in range(c, d + 1):
                    if grid[i][j] == 1:
                        lx = min(lx, j)   
                        ly = max(ly, j)   
                        ty = min(ty, i)   
                        dy = max(dy, i)   
            if lx == cols:  
                return 0
            return (ly - lx + 1) * (dy - ty + 1)

        ans = int(1e9)

        
        for i in range(rows):
            for j in range(cols):
                ans = min(
                    ans,
                    area(0, i, 0, cols - 1) + area(i + 1, rows - 1, 0, j) + area(i + 1, rows - 1, j + 1, cols - 1),
                    area(0, i, 0, j) + area(0, i, j + 1, cols - 1) + area(i + 1, rows - 1, 0, cols - 1),
                    area(0, rows - 1, 0, j) + area(0, i, j + 1, cols - 1) + area(i + 1, rows - 1, j + 1, cols - 1),
                    area(0, rows - 1, j + 1, cols - 1) + area(0, i, 0, j) + area(i + 1, rows - 1, 0, j)
                )

        
        for i in range(rows):
            for j in range(i, rows):
                ans = min(
                    ans,
                    area(0, i, 0, cols - 1) + area(i + 1, j, 0, cols - 1) + area(j + 1, rows - 1, 0, cols - 1)
                )

        
        for i in range(cols):
            for j in range(i, cols):
                ans = min(
                    ans,
                    area(0, rows - 1, 0, i) + area(0, rows - 1, i + 1, j) + area(0, rows - 1, j + 1, cols - 1)
                )

        return ans


sol = Solution()

grid1 = [
    [0,0,0,1,0],
    [0,0,1,0,1],
    [1,0,0,0,0],
    [0,1,1,0,0]
]
print(sol.minimumSum(grid1))

grid2 = [
    [1,1,1]
]
print(sol.minimumSum(grid2))

grid3 = [
    [1,1],
    [1,1]
]
print(sol.minimumSum(grid3))

grid4 = [
    [1,0,0,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0],
    [1,0,0,0,1]
]
print(sol.minimumSum(grid4))

grid5 = [
    [0,0],
    [0,0]
]
print(sol.minimumSum(grid5))
