class FoodRatings {
public:
    unordered_map<string, set<pair<int,string>>> mp;
    unordered_map<string, int> fr;
    unordered_map<string, string> fc;
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (int i = 0; i < foods.size(); i++) {
            string food = foods[i],
                cuisine = cuisines[i];
            int rating = ratings[i];
            mp[cuisine].insert({-rating, food});
            fr[food] = rating;
            fc[food] = cuisine;
        }
    }
    
    void changeRating(string food, int newRating) {
        string cuisine = fc[food];
        int oldRating = fr[food];
        mp[cuisine].erase({-oldRating, food});
        mp[cuisine].insert({-newRating, food});
        fr[food] = newRating;
    }
    
    string highestRated(string cuisine) {
        return (mp[cuisine].begin())->second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */