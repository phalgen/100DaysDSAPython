"""You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.

 

Example 1:

Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
Output: [1,2,3,4,5,6]
Explanation: Here, nums[2] == key and nums[5] == key.
- For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. Thus, 0 is not a k-distant index.
- For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
- For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
- For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
- For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
- For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
- For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
Thus, we return [1,2,3,4,5,6] which is sorted in increasing order."""


class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        l=[]
        for i in range(0, len(nums)):
            if(nums[i]==key):
                l.append(i)

        result=set()

        for i in range(0, len(nums)):
            for j in l:
                if(abs(i-j)<=k):
                    result.add(i)
                    
        

        return sorted(list(result))
    
print(Solution().findKDistantIndices([1,2,3,4,5], 3, 1))
print(Solution().findKDistantIndices([1,2,3,4,5], 2, 2))
print(Solution().findKDistantIndices([5,5,5,5,5], 5, 0))
print(Solution().findKDistantIndices([1,2,3,2,1], 2, 1))
print(Solution().findKDistantIndices([1,2,1,2,1,2], 2, 2))
print(Solution().findKDistantIndices([1,1,1,1,1], 1, 3))
print(Solution().findKDistantIndices([7,8,9,8,7], 9, 1))
print(Solution().findKDistantIndices([9,1,2,3,1,9,1,2], 9, 2))
print(Solution().findKDistantIndices([4,3,4,3,4], 3, 0))
print(Solution().findKDistantIndices([6,5,4,3,2,1], 1, 5))
