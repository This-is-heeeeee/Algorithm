#include <iostream>
#include <string.h>

using namespace std;

int chapter[500];
long long buf[500][500];

long long func(int s, int k){
    long long min = 1000000000;
    long long temp;
    long long total = 0;
    int m1, m2;
    
    if(s == k) return buf[s][k] = chapter[s];
    if(buf[s][k] >= 0) return buf[s][k];
    
    for(int i = s; i <= k; i++) total += chapter[i];
    
    for(int i = s; i < k; i++){
        m1 = m2 = 0;
        if(s == i) m1 = chapter[i];
        if(i+1 == k) m2 = chapter[i+1];
        temp = func(s,i) + func(i+1,k) + (total - m1 - m2);
        if(min > temp)
            min = temp;
    }
    buf[s][k] = min;
    return buf[s][k];
}

int main(int argc, const char * argv[]) {
    int T;
    int k;
    
    cin >> T;
    
    for(int test_case = 0; test_case < T; test_case++){
        cin >> k;
        
        for(int i = 0; i < k; i++){
            cin >> chapter[i];
        }
        
        memset(buf,-1,sizeof(buf));
        
        cout << func(0,k-1) << "\n";
    }
    return 0;
}
