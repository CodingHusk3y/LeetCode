class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for string in strs:
            group[tuple(sorted(string))].append(string)

        return [anagrams for anagrams in group.values()]