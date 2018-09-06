#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    string str;
    stack<int> stc;
    int sum;
    
    cin >> str;
    
    for(int i = 0; i < str.length(); i++){
        if(str.at(i) == '(' || str.at(i) == '[')
            stc.push(str.at(i));
        else if(str.at(i) == ')'){
            sum = 0;
            if(stc.empty()){
                cout << "0\n";
                return 0;
            }
            if(stc.top() == '('){
                stc.pop();
                stc.push(2);
            }
            else if(stc.top() == '['){
                cout << "0\n";
                return 0;
            }
            else{
                while(stc.top() != '('){
                    sum += stc.top();
                    stc.pop();
                    if(stc.empty()){
                        cout << "0\n";
                        return 0;
                    }
                }
                stc.pop();
                stc.push(sum*2);
            }
        }
        else if(str.at(i) == ']'){
            sum = 0;
            if(stc.empty()){
                cout << "0\n";
                return 0;
            }
            if(stc.top() == '['){
                stc.pop();
                stc.push(3);
            }
            else if(stc.top() == '('){
                cout << "0\n";
                return 0;
            }
            else{
                while(stc.top() != '['){
                    sum += stc.top();
                    stc.pop();
                    if(stc.empty()){
                        cout << "0\n";
                        return 0;
                    }
                }
                stc.pop();
                stc.push(sum*3);
            }
        }
    }
    sum = 0;
    while(!stc.empty()){
        if(stc.top() == '(' || stc.top() == '['){
            cout << "0\n";
            return 0;
        }
        sum += stc.top();
        stc.pop();
    }
    cout << sum << "\n";
    return 0;
}
