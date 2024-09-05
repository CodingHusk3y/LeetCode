class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        first = min(strs)
        last = max(strs)

        # Find the common prefix between first and last.
        length = min(len(first), len(last))
        for i in range(length):
            if first[i] != last[i]:
                return first[0:i]

        return first[0:length]