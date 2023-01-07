class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = [a-b for a,b in zip(gas,cost)]
        # print(arr)
        n = len(arr)
        s = 0
        i = 0
        res = -1
        while 1:
            s += arr[i]
            if i == res and s >= 0:
                return res+1
            
            if s < 0:
                if res >= i:
                    return -1
                s = 0
                res = i
            i += 1
            if i == n:
                if res == -1:
                    return 0
                i = 0
        return 0