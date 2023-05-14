class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        odd_s = 0
        even_s = 0
        for i in range(n):
            odd_s,even_s = even_s + arr[i] * ((i+2)//2), odd_s + arr[i] * ((i+1)//2)
            res += odd_s
        return res