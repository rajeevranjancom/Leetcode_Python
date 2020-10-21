"""
Premium Question
https://leetcode.com/problems/palindrome-permutation/
Author: Rajeev Ranjan

"""
from collections import defaultdict

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = defaultdict(int)
        for c in s:
            m[c] += 1

        once = False
        for v in m.values():
            if v % 2 == 1:
                if once:
                    return False
                once = True

        return True
