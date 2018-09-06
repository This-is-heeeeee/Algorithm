#include <iostream>
#include <stack>

using namespace std;

int main(int argc, const char * argv[]) {
    
    stack<int> s;
    int N;
    string func;
    int num;
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        cin >>func;
        
        if(func == "push"){
            cin >> num;
            s.push(num);
        }
        else if(func == "pop")  {
            if(!s.empty()){
                cout << s.top() << "\n";
                s.pop();
            }
            else cout << "-1" << "\n";
        }
        else if(func == "size") cout<<s.size() << "\n";
        else if(func == "empty")    cout<<s.empty() << "\n";
        else if(func == "top"){
            if(!s.empty())
                cout<<s.top() << "\n";
            else cout << "-1\n";
        }
    }
    return 0;
}
