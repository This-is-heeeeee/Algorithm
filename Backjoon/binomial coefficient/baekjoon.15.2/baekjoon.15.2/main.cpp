#include <iostream>

using namespace std;

unsigned long long buf[1000][1001] = {0,};

unsigned long long func(int a, int b){
    if(buf[a-1][b] != 0) return buf[a-1][b];
    else{
        if(a == b || b == 0) buf[a-1][b] = 1;
        else if(b == a-1 || b == 1) buf[a-1][b] =  a;
        else buf[a-1][b] = (func(a-1,b-1) + func(a-1,b))%10007;
        buf[a-1][a-b] = buf[a-1][b];
        return buf[a-1][b];
    }
}

int main(int argc, const char * argv[]) {
    unsigned long long Answer;
    int n1, n2;
    
    cin >> n1 >> n2;
    
    Answer  = func(n1, n2);
    
    cout << Answer << "\n";
    return 0;
}
