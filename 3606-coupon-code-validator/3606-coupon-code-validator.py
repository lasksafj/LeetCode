class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        for cod,b,a in zip(code, businessLine,isActive):
            if cod and all(c.isalnum() or c == '_' for c in cod) and a and b in ["electronics", "grocery", "pharmacy", "restaurant"]:
                res.append([cod, b])
        mp={"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        return [cod for cod,_ in sorted(res, key=lambda e: [mp[e[1]], e[0]])]