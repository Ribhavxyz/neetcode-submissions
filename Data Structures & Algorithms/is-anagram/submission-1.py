class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count_letters(s):
            counts = {}
            for letter in s:
                if letter in counts:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
            return counts
        if len(s) != len(t):
            return False
        return count_letters(s) == count_letters(t) 
