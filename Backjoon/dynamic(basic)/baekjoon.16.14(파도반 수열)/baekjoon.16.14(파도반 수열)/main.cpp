#include <iostream>

using namespace std;

long long wave[100] = {1,1,1,2,2,};

long long func(int n){
    if(wave[n-1] > 0) return wave[n-1];
    
    wave[n-1] = func(n-1) + func(n-5);
    
    return wave[n-1];
}

int main(int argc, const char * argv[]) {
    int t;
    int n;
    
    cin >> t;
    
    for(int test_case = 0; test_case < t; test_case++){
        cin >> n;
    
    cout << func(n) << "\n";
    }
    return 0;
}
