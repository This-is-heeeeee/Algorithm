#include <iostream>
#include <stack>

using namespace std;

int main(int argc, const char * argv[]) {
    stack<int> s;
    int N;
    int sequence[100000];
    int index = 0;
    int num = 1;
    int max = 0;
    int check = 0;
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        cin >>sequence[i];
        if(sequence[i] > max) max = sequence[i];
        if(i-1>=0 && sequence[i] > sequence[i-1] && sequence[i] < max) check++;
    }
    
    if(check >= 1){cout << "NO\n"; return 0;}
    
    while(index < N){
        if(!s.empty() > 0 && sequence[index] == s.top()){
            s.pop();
            cout << "-\n";
            index++;
        }
        else{
            s.push(num);
            cout << "+\n";
            num++;
        }
    }
    
    return 0;
}
