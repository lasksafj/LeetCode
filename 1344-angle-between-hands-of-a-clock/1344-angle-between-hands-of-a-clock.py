class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        pmin = minutes/60
        hour = (hour+pmin)%12
        h_angle = hour*30
        m_angle = minutes*6
        a = abs(h_angle-m_angle)
        return min(a, 360-a)