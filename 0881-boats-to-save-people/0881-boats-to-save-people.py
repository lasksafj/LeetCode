class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res,l,r = 0,0,len(people)-1
        while l <= r:
            res += 1
            if limit - people[r] >= people[l]:
                l += 1
            r -= 1
        return res