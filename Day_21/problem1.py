"""Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given 
researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if(len(citations)==1):
            if citations[0]>0:
                return 1
            else:
                return 0

        


        max1=max(citations)

        citations.sort()

        count=0
        for i in range(len(citations)):
            for j in range(len(citations)):
                if(max1==citations[j]):
                    count = count+1


            if(count>= max1):
                return max1

            else:
                citations = [x for x in citations if x !=max1]
                max1=max(citations)