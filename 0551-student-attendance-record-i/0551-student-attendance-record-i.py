class Solution:
    def checkRecord(self, s: str) -> bool:

        # Total absences 2 ya usse zyada nahi hone chahiye
        if s.count('A') >= 2:
            return False

        # 3 consecutive L check karenge
        if 'LLL' in s:
            return False

        return True