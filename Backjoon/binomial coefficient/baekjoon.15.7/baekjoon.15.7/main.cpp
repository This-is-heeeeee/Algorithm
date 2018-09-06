#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    unsigned long long Answer;
    long n1, n2;
    
    while(1){
        cin >> n1 >> n2;
        
        if(n1 == 0 && n2 == 0) break;
        Answer = 1;
        
        if(n2 < n1/2) n2 = n1-n2;
        
        for(long i = 1; i <= n1 - n2; i++){
            Answer = Answer * (n1-i+1) / i;
        }
    
        cout << Answer << "\n";
    }
    return 0;
}
