"""A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

 

Example 1:

Input: k = 2, n = 5
Output: 25
Explanation:
The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
  base-10    base-2
    1          1
    3          11
    5          101
    7          111
    9          1001
Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
"""


class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def is_palindrome(s):
            return s == s[::-1]
        
        def to_base_k(num, k):
            if num == 0:
                return "0"
            digits = []
            while num > 0:
                digits.append(str(num % k))
                num //= k
            return ''.join(reversed(digits))

        def generate_palindromes():
            length = 1
            while True:
                if length == 1:
                    for d in range(1, 10):
                        yield d
                else:
                    half_len = length // 2
                    start = 10**(half_len - 1)
                    end = 10**half_len
                    if length % 2 == 0:
                        for half in range(start, end):
                            s = str(half)
                            yield int(s + s[::-1])
                    else:
                        for half in range(start, end):
                            s = str(half)
                            for mid in '0123456789':
                                yield int(s + mid + s[::-1])
                length += 1

        total = 0
        count = 0
        for p in generate_palindromes():
            if is_palindrome(to_base_k(p, k)):
                total += p
                count += 1
                if count == n:
                    return total
        return total

print(Solution().kMirror(2, 5))       
print(Solution().kMirror(3, 7))       
print(Solution().kMirror(7, 17))      
print(Solution().kMirror(10, 1))       
print(Solution().kMirror(2, 1))        

