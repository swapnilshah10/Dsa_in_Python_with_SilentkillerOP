class Solution {
public:
    string reverseWords(string s) {
        string ans = "";
        int i = 0;
        int n = s.length();
        stack <char>st;
        while(i < n){
            if(s[i]==' '){
                ans += ' ';
                while(!st.empty()){
                    ans+=st.top();
                    st.pop();
                }
            }
            else st.push(s[i]);
            i+=1;
        }
        if(!st.empty()) ans+=' ';
        while(!st.empty()){
            ans += st.top();
            st.pop();
        }
        ans.erase(0,1);
        return ans;
    }
};