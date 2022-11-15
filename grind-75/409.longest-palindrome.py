from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0

        count = Counter(s)

        res = 0
        extra = False
        for _, char_count in count.items():
            if char_count % 2 == 0:
                res += char_count
            else:
                res += char_count - 1
                extra = True

        return res + 1 if extra else res
