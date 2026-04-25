class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()
        
        for charS in s:
            if charS in hashmap:
                hashmap[charS] += 1
            else:
                hashmap[charS] = 1
        
        # hashmap is filled with the number of occurences
        # { r: 2, a: 2, c: 2, e: 1 }

        # loop through the second string (t)
        for charT in t:
            if charT in hashmap:
                if hashmap[charT] == 1:
                    del hashmap[charT]
                else:
                    hashmap[charT] -= 1
            else:
                return False
        
        if hashmap == dict():
            return True
        else:
            return False
        