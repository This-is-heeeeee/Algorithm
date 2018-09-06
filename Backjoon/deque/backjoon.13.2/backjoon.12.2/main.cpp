#include <iostream>
#include <deque>

using namespace std;

deque<int> dq;
int buf;

void func1(){
    dq.pop_front();
}

void func2(){
    buf = dq.front();
    dq.pop_front();
    dq.push_back(buf);
    
}

void func3(){
    buf = dq.back();
    dq.pop_back();
    dq.push_front(buf);
}

int main(int argc, const char * argv[]) {
    int N, M;
    int count = 0, num, check;
    
    cin >> N >> M;
    
    for(int i = 1; i <= N; i++)
        dq.push_back(i);
    
    for(int i = 0; i < M; i++){
        cin >> num;
        while(1){
            if(dq.front() == num){
                func1();
                break;
            }
            else{
                check = -1;
                for(int j = 0; j < dq.size()/2+1; j++)
                    if(dq[j] == num) check = 1;
                if(check == 1){
                    func2();
                }
                else{
                    func3();
                }
                count++;
            }
        }
    }
    
    cout << count << "\n";
    return 0;
}
