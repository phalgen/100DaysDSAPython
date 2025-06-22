"""You are given a string word and an integer k.

We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.

Here, freq(x) denotes the frequency of the character x in word, and |y| denotes the absolute value of y.

Return the minimum number of characters you need to delete to make word k-special.

 

Example 1:

Input: word = "aabcaba", k = 0

Output: 3

Explanation: We can make word 0-special by deleting 2 occurrences of "a" and 1 occurrence of "c". Therefore, word becomes equal to "baba" where freq('a') == freq('b') == 2.
"""


class Solution(object):
    def minimumDeletions(self, word, k):
        d = {}
        for ch in word:
            d[ch] = d.get(ch, 0) + 1

        freq = list(d.values())
        ans = float('inf')

        for target in range(1, max(freq) + 1):
            deletions = 0
            for f in freq:
                if f < target:
                    deletions += f
                elif f > target + k:
                    deletions += f - (target + k)
            ans = min(ans, deletions)

        return ans
