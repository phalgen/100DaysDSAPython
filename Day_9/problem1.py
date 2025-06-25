"""Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
 

Example 1:

Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8
Explanation: The 2 smallest products are:
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
The 2nd smallest product is 8."""


import bisect
import math

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        nums1.sort()
        nums2.sort()

        def count_less_equal(x):
            count = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        count += len(nums2)
                elif a > 0:
                    # We want b <= x // a
                    count += bisect.bisect_right(nums2, x // a)
                else:  # a < 0
                    # We want b >= ceil(x / a)
                    low = math.ceil(float(x) / a)
                    idx = bisect.bisect_left(nums2, low)
                    count += len(nums2) - idx
            return count

        left = -10**10
        right = 10**10
        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
print(Solution().kthSmallestProduct([1, 2], [3, 4], 3))
print(Solution().kthSmallestProduct([-4, -2, 0, 3], [-2, -1], 6))
print(Solution().kthSmallestProduct([-6], [-9], 1))
print(Solution().kthSmallestProduct([1, 3, 5], [2, 4, 6], 4))
print(Solution().kthSmallestProduct([-5, -2, 0, 1], [-3, -1, 2], 5))
