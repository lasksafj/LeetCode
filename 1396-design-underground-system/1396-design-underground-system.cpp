class UndergroundSystem {
public:
    unordered_map<int,pair<int,string>> m;
    unordered_map<string, pair<int, int>> avg;
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        m[id] = {t, stationName};
    }
    
    void checkOut(int id, string stationName, int t) {
        auto [startTime, startStation] = m[id];
        string s = startStation + ' ' + stationName;
        avg[s] = {avg[s].first + t - startTime, avg[s].second + 1};
    }
    
    double getAverageTime(string startStation, string endStation) {
        string s = startStation + ' ' + endStation;
        return avg[s].first * 1.0 / avg[s].second;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */