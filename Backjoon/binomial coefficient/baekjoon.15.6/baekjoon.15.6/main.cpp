#include <iostream>
#include <math.h>

using namespace std;

unsigned long long d = 1000000000000000;

struct bigint{
    unsigned long long high = 0;
    unsigned long long low = 1;
};

bigint operator+(bigint a, bigint b){
    bigint c;
    c.high = a.high + b.high;
    c.low = a.low + b.low;
    if(c.low > d){
        c.high += (c.low/d);
        c.low %= d;
    }
    return c;
}

int main(int argc, const char * argv[]) {
    int n1, n2;
    bigint a[100][101];
    
    cin >> n1 >> n2;
    
    n2 = (n2 < n1-n2) ? n2:(n1-n2);
    
    for(int i = 1; i < n1; i++){
        int k = (i < n2) ? i : n2;
        for(int j = 1; j <= k; j++){
            a[i][j] = a[i-1][j-1] + a[i-1][j];
        }
    }
    
    if(a[n1-1][n2].high > 0)
        cout << a[n1-1][n2].high;
    cout << a[n1-1][n2].low << "\n";
    
    return 0;
}
//100C50은 100891344545564193334812497256입니다.
