#include <iostream>
#include <deque>

using namespace std;

int main(int argc, const char * argv[]) {
    deque<int> dq;
    string inst;
    int num;
    
    int N;
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        cin >> inst;
        if(inst == "push_front" || inst == "push_back"){
            cin >> num;
            //dq.push_front(num);
            (inst=="push_front") ? dq.push_front(num):dq.push_back(num);
        }
        else if(inst == "pop_front" || inst == "pop_back"){
            if(dq.empty()) cout << "-1\n";
            else{
                num = (inst=="pop_front") ? dq.front():dq.back();
                cout << num << "\n";
                (inst=="pop_front") ? dq.pop_front():dq.pop_back();
            }
        }
        else if(inst == "size") cout <<dq.size() << "\n";
        else if(inst == "empty") cout << dq.empty() << "\n";
        else if(inst == "front" || inst == "back"){
            if(dq.empty()) cout << "-1\n";
            else{
                num = (inst=="front") ? dq.front():dq.back();
                cout << num << "\n";
            }
        }
    }
    return 0;
}
