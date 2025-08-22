class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()  # track dupes
        streak = 0
        longest = 0
        substr = ""
        for c in s:
            if c in seen:
                while c in seen:
                    seen.remove(substr[0])
                    substr = substr[1:]
                seen.add(c)
                substr += c
                streak = len(substr)
            else:
                seen.add(c)
                substr += c
                streak += 1

            longest = max(longest, len(substr))

        return longest