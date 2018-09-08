#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int coin[100] = {0,};
    int d[10001] = {0,};
    int n, k;

    cin >> n >> k;
    
    for(int i = 0; i < n; i++){
        cin >> coin[i];
    }
    
    d[0] = 1;
    
    for(int i = 0; i < n; i++){
        for(int j = coin[i]; j <= k; j++){
            d[j] += d[j-coin[i]];
        }
    }
    
    cout << d[k] << "\n";
    return 0;
}
