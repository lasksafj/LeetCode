class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = defaultdict(int)
        for cpdomain in cpdomains:
            n,domains = cpdomain.split()
            n = int(n)
            domains = domains.split('.')
            for i in range(len(domains)):
                mp['.'.join(domains[i:])] += n
        return [str(b) + ' ' + a for a,b in mp.items()]