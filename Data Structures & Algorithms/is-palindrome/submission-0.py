class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_n = "abcdefghijklmnopqrstuvwxyz0123456789"
        compact_s = ""

        for cha in s:
            if cha.lower() in alpha_n:
                compact_s += cha.lower()

        if compact_s == compact_s[::-1]:
            return True
        else:
            return False

        