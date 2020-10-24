#!/usr/bin/python3
"""
Given a rows x cols screen and a sentence represented by a list of non-empty
words, find how many times the given sentence can be fitted on the screen.

Note:
A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
Author: Rajeev Ranjan

"""
from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        How many times to fit

        Combine the words in to a string and wrap it around
        """
        sentence = " ".join(sentence) + " "  # unify the condition checking for the last word; tail will wrap with head with space
        i = 0
        for r in range(rows):
            i += cols
            while sentence[i % len(sentence)] != " ":
                i -= 1

            # now sentence[i] is " "
            i += 1

        ret = i // len(sentence)
        return ret 