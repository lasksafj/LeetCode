class Solution {
public:
    int calculate(string s) {
        stack<int> nums;
        stack<char> op;
        nums.push(0);
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                int n = s[i] - '0';
                while (isdigit(s[++i])) {
                    n = n*10 + (s[i] - '0');
                }
                --i;
                nums.push(n);
            }
            else if (s[i] == '(') {
                op.push(s[i]);
                int j = i+1;
                while (s[j] == ' ')
                    j++;
                if (s[j] == '-')
                    nums.push(0);
            }
                
            else if (s[i] == ')') {
                while (op.top() != '(')
                    process(nums, op);
                op.pop();
            }
            else if (s[i] == '+' || s[i] == '-') {
                if (!op.empty() && op.top() != '(') 
                    process(nums, op);
                op.push(s[i]);
            }
        }
        while (!op.empty())
            process(nums, op);
        return nums.top();
    }
    
    void process(stack<int>& nums, stack<char>& op) {
        int result = 0;
        int a = nums.top();
        nums.pop();
        int b = nums.top();
        nums.pop();
        if (op.top() == '+')
            result = b + a;
        else
            result = b - a;
        // cout << b << op.top() << a << "=" << result << endl;
        op.pop();
        nums.push(result);
    }
};