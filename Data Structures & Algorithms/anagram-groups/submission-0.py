class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            sortedS = "".join(sorted(i))
            groups[sortedS].append(i)
        return list(groups.values())