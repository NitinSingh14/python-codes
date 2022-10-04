def lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    l = 0
    ml = 0
    for r, ch in enumerate(s):
        if ch in seen:
            if seen[ch] >= l:
                l = seen[ch] + 1
        ml = max(r-l+1, ml)
        seen[ch] = r
    return ml
