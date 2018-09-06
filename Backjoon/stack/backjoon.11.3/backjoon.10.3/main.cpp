#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    stack<int> s;
    string ps;
    int N;
    bool check;
    
    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> ps;
        check = true;
        for(int j = 0; j < ps.length(); j++){
            if(ps.at(j) == '(') s.push(1);
            else{
                if(s.empty()){check = false; break;}
                s.pop();
            }
        }
        
        if(s.empty() && check) cout << "YES\n";
        else cout << "NO\n";
        
        while(!s.empty()) s.pop();
    }
    
    return 0;
}
