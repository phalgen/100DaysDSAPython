"""Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105

"""
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1  

        for i in range(m * n):
            result.append(mat[row][col])

            if direction == 1:  
                if col == n - 1:  
                    row += 1
                    direction = -1
                elif row == 0:  
                    col += 1
                    direction = -1
                else:  
                    row -= 1
                    col += 1
            else:  
                if row == m - 1:  
                    col += 1
                    direction = 1
                elif col == 0:  
                    row += 1
                    direction = 1
                else:  
                    row += 1
                    col -= 1

        return result
    

sol = Solution()

print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.findDiagonalOrder([[1,2],[3,4]]))
print(sol.findDiagonalOrder([[1,2,3,4]]))
print(sol.findDiagonalOrder([[1],[2],[3],[4]]))
print(sol.findDiagonalOrder([[1,2,3,4],[5,6,7,8]]))
print(sol.findDiagonalOrder([[1,2],[3,4],[5,6],[7,8]]))
print(sol.findDiagonalOrder([[42]]))
print(sol.findDiagonalOrder([[1,-2,3],[-4,5,-6],[7,-8,9]]))

mat = [[i + j*5 for i in range(1,6)] for j in range(5)]
print(sol.findDiagonalOrder(mat))

