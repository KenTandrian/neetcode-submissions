class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in hashmap:
                hashmap[sortedStr].append(s)
            else:
                hashmap[sortedStr] = [s]
        
        return list(hashmap.values())
