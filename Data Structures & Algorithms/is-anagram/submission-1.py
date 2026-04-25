class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()
        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        for c in t:
            if c in hashmap:
                if hashmap[c] == 1:
                    del hashmap[c]
                else:
                    hashmap[c] -= 1
            else:
                return False

        if hashmap == dict():
            return True
        else:
            return False