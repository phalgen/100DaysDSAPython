"""You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise."""


class Solution(object):
    def judgePoint24(self, cards):
        cards = list(map(float, cards)) 
        def dfs(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24.0) < 1e-6

            n = len(cards)
            for i in range(n):
                for j in range(i + 1, n):  
                    a, b = cards[i], cards[j]
                    rest = [cards[k] for k in range(n) if k != i and k != j]

                    results = [
                        a + b,
                        a - b, b - a,
                        a * b
                    ]
                    if abs(b) > 1e-6: results.append(a / b)
                    if abs(a) > 1e-6: results.append(b / a)

                    for val in results:
                        if dfs(rest + [val]):
                            return True
            return False

        return dfs(cards)


s = Solution()
cards = [8, 1, 6, 6]
print("Can make 24?", s.judgePoint24(cards))