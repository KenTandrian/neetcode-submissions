class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s="No lemon, no melon"
        left, right = 0, len(s) - 1 # 0, 17

        while left < right:
            # skip non alphanumeric
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            # now that it is alphanumeric, compare!
            if s[left].lower() != s[right].lower():
                return False
            
            # Move inward
            left += 1
            right -= 1
        return True
