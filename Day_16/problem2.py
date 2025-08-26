class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        longest = 0
        area = 0
        
        for a, b in dimensions:   
            diagonal_sq = a*a + b*b
            if diagonal_sq > longest:
                longest = diagonal_sq
                area = a * b
            elif diagonal_sq == longest:  
                area = max(area, a * b)

        return area
