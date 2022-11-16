class Solution:
    def findItinerary(self, tickets):
        nextto = collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            nextto[a].append(b)
        res = []
        
        def dfs(i):
            while nextto[i]:
                dfs(nextto[i].pop())
            res.append(i)
        dfs('JFK')
        return res[::-1]