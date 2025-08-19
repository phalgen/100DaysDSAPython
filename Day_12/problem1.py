"""Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
"""


class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count =0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count=count+1

            if nums[i]!=0:
                ans+=(count*(count+1))//2
                count=0

        ans+=(count*(count+1))//2
        return ans
    

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0,0,1,0,0,0], 9),
        ([0,0,0], 6),
        ([1,2,3], 0),
        ([0,1,0,0,2,0], 5),
        ([0,0,0,0], 10),
        ([], 0)
    ]

    for nums, expected in tests:
        result = sol.zeroFilledSubarray(nums)
        print(f"nums = {nums} -> {result} (expected {expected})")
