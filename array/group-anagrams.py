class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in groups:
                groups[sorted_string] = []

            groups[sorted_string].append(string)

        return groups.values()