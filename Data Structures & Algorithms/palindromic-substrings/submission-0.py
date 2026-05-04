class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        def expand(start, end):
            total = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                total += 1
            return total
        res = 0
        for i in range(len(s)):
            res += expand(i, i)
            res += expand(i, i + 1)
        return res