"""
3021. Alice and Bob Playing Flower Game
Solved
Medium
Topics
premium lock icon
Companies
Hint
Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are x flowers in the first lane between Alice and Bob, and y flowers in the second lane between them.



The game proceeds as follows:

Alice takes the first turn.
In each turn, a player must choose either one of the lane and pick one flower from that side.
At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

Alice must win the game according to the described rules.
The number of flowers x in the first lane must be in the range [1,n].
The number of flowers y in the second lane must be in the range [1,m].
Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

 

Example 1:

Input: n = 3, m = 2
Output: 3
Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).


"""


class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        odd_x,even_x,odd_y,even_y=0,0,0,0

        if(n%2==0):
            odd_x=even_x=n/2

        else:
            odd_x=(n+1)/2
            even_x=(n-1)/2

        if(m%2==0):
            odd_y=even_y=m/2

        else:
            odd_y=(m+1)/2
            even_y=(m-1)/2

        answer=odd_x*even_y+even_x*odd_y

        return answer

sol = Solution()

print(sol.flowerGame(1, 1))
print(sol.flowerGame(1, 2))
print(sol.flowerGame(2, 2))
print(sol.flowerGame(3, 3))
print(sol.flowerGame(3, 4))
print(sol.flowerGame(4, 4))
print(sol.flowerGame(5, 5))
print(sol.flowerGame(10, 10))
