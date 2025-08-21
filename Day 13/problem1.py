class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]
        total = 0

        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j-1] + 1

        
        for i in range(m):
            for j in range(n):
                if dp[i][j] > 0:
                    width = dp[i][j]
                    for k in range(i, -1, -1):
                        width = min(width, dp[k][j])
                        if width == 0:
                            break
                        total += width

        return total



sol = Solution

print(sol.numSubmat([[1,0,1],[1,1,0],[1,1,0]]))