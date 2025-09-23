class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(max(len(v1), len(v2))):
            try:
                a = int(v1[i])
            except:
                a = 0
            try:
                b = int(v2[i])
            except:
                b = 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0