from sortedcontainers import SortedList
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        nouse = [0]*n
        use = SortedList()
        free_room = SortedList(range(n))
        # print(meetings)
        # print(free_room)
        for a,b in meetings:
            while use and use[0][0] <= a:
                free_room.add(use[0][1])
                use.discard(use[0])

            if free_room:
                use.add((b, free_room[0]))
                nouse[free_room[0]] += 1
                free_room.discard(free_room[0])
            else:
                endtime, room = use[0]
                use.discard(use[0])
                use.add( (b+max(0,endtime-a), room) )
                nouse[room] += 1
        ma = -1
        res = 0
        for i,n in enumerate(nouse):
            if n > ma:
                ma = n
                res = i
        return res