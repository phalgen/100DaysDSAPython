"""You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
 

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Explanation:



The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

[7, 2] becomes [2, 7].
[3] remains unchanged.

"""

class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n= len(grid)

        for i in range(n):
            tmp=[grid[i+j][j] for j in range(n-i)]
            tmp.sort(reverse=True)
            for j in range(n-i):
                grid[i+j][j]=tmp[j]

        
        for i in range(1,n):
            tmp=[grid[j][i+j] for j in range(n-i)]
            tmp.sort()
            for j in range(n-i):
                grid[j][i+j]=tmp[j]

        return grid
        
