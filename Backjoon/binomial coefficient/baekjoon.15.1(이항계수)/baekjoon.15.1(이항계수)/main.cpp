#include <iostream>

using namespace std;

long long Func(int n1, int n2){
    if(n1 == n2) return 1;
    else return n1*Func(n1-1, n2);
}

int main(int argc, const char * argv[]) {
    
    int n1, n2;
    long long Answer;
    
    cin >> n1 >> n2;
    
    Answer = Func(n1,n2) /Func(n1-n2, 1);
    
    cout << Answer <<"\n";
    return 0;
}
