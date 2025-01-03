class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            current_str = ''.join(sorted(string))

            groups[current_str].append(string)

        return list(groups.values())