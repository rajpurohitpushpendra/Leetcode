class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        first = len(s) % k
        groups = []

        if first:
            groups.append(s[:first])

        for i in range(first, len(s), k):
            groups.append(s[i:i + k])

        return "-".join(groups)