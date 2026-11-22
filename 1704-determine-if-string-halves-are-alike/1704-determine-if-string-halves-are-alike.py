class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        mid = len(s) // 2
        return sum(c in vowels for c in s[:mid]) == sum(c in vowels for c in s[mid:])