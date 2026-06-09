class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for str in strs:
            sorted_str = sorted(str)
            group[tuple(sorted_str)].append(str)
        # print(group)
        return list(group.values())
