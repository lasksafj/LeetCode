class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        m = defaultdict(int)
        ma = 0
        for i in range(len(messages)):
            m[senders[i]] += len(messages[i].split(' '))
            if m[senders[i]] > ma:
                ma = m[senders[i]]
        return sorted([(b,a) for a,b in m.items()], reverse=True)[0][1]