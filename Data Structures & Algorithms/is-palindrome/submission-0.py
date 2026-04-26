class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "Was it a car or a cat I saw?"
        clean_str = "".join([char for char in s if char.isalnum()])
        # s = "WasitacaroracatIsaw"
        length = len(clean_str) # 19

        for i in range(0, int(length/2)):
            if clean_str[i].lower() == clean_str[length-i-1].lower():
                continue
            else:
                return False
        return True
        