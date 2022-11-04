class Solution {
public:
    bool isVowel(char c) {
        return c == 'a' || c == 'i' || c == 'e' || c == 'o' || c == 'u'
            || c == 'A' || c == 'I' || c == 'E' || c == 'O' || c == 'U';
    }
    
    string reverseVowels(string s) {
        int i=0, j=s.size()-1;
        while (i < j) {
            while (i < j && !isVowel(s[i]))
                i++;
            while (i < j && !isVowel(s[j]))
                j--;
            if (i < j)
                swap(s[i++], s[j--]);
        }
        return s;
    }
};