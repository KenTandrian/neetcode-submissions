class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "Was it a car or a cat I saw?"
        clean_str = "".join([char.lower() for char in s if char.isalnum()])
        # s = "WasitacaroracatIsaw"
        return clean_str == clean_str[::-1]
