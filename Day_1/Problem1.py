"""
Day 1 problem is as follows:
You are given three integers n, m, k. A good array arr of size n is defined as follows:

Each element in arr is in the inclusive range [1, m].
Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, m = 2, k = 1

Output: 4

Explanation:

There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
Hence, the answer is 4.
Example 2:

Input: n = 4, m = 2, k = 2

Output: 6

Explanation:

The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
Hence, the answer is 6.
Example 3:

Input: n = 5, m = 2, k = 0

Output: 2

Explanation:

The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
 

Constraints:

1 <= n <= 105
1 <= m <= 105
0 <= k <= n - 1"""
class Solution(object):
    def countGoodArrays(self, n, m, k):
        MOD = 10**9 + 7

        def mod_pow(x, y):
            res = 1
            while y:
                if y % 2:
                    res = res * x % MOD
                x = x * x % MOD
                y //= 2
            return res

        def mod_inv(x):
            return mod_pow(x, MOD - 2)

        fact = [1] * n
        inv_fact = [1] * n

        for i in range(1, n):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[n - 1] = mod_inv(fact[n - 1])
        for i in range(n - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        return m * comb(n - 1, k) % MOD * mod_pow(m - 1, n - 1 - k) % MOD



sol = Solution()
print(sol.countGoodArrays(3, 2, 1))  # Output: 4
print(sol.countGoodArrays(2, 2, 1))  # Output: 2 ([1,1], [2,2])
print(sol.countGoodArrays(2, 2, 0))  # Output: 2 ([1,2], [2,1])
print(sol.countGoodArrays(4, 2, 2))  # Output: 2 ([1,1,1,2], [2,2,2,1])
print(sol.countGoodArrays(1, 3, 0))  # Output: 3 (any of [1], [2], [3])
print(sol.countGoodArrays(5, 3, 0))  # Output: 48 (no equal adjacents)
print(sol.countGoodArrays(5, 3, 4))  # Output: 3 (must be all same [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3])