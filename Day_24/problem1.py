"""Given a 0-indexed string s, permute s to get a new string t such that:

All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

 

Example 1:

Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places."""


class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        dict1 = {
            'A': 65, 'E': 69, 'I': 73, 'O': 79, 'U': 85,
            'a': 97, 'e': 101, 'i': 105, 'o': 111, 'u': 117
        }

        def compare(ch):
            return(dict1[ch],ord(ch))

        vowels =[ch for ch in s if ch in dict1]

        vowels.sort(key=compare)

        result=[]
        i=0

        for ch in s:
            if ch in dict1:
                result.append(vowels[i])
                i=i+1
            else:
                result.append(ch)

        return "".join(result)
                






        