#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int rate[1000] = {0,};
int dp[1000] = {0,};
vector<int> vec_b[1000];
int T, test_case;
int N, K;
int n1, n2;
int f;

int func(int n){
    if(dp[n-1] >= 0) return dp[n-1];
    if(vec_b[n-1].empty()){
        dp[n-1] = rate[n-1];
    }
    else{
        for(int i = 0; i < vec_b[n-1].size(); i++){
            if(dp[n-1] < func(vec_b[n-1][i]) + rate[n-1]){
                dp[n-1] = func(vec_b[n-1][i]) + rate[n-1];
            }
        }
    }
    vec_b[n-1].clear();
    return dp[n-1];
}

int main(int argc, const char * argv[]) {
    
    cin >> T;
    for(test_case = 0; test_case<T; test_case++){
        cin >> N >> K;
        
        for(int i = 0; i < N; i++){
            cin >> rate[i];
        }
        
        for(int i = 0; i < K; i++){
            cin >> n1 >> n2;
            vec_b[n2-1].push_back(n1);
        }
        
        cin >> f;
        
        fill_n(dp,N,-1);
        
        cout << func(f) << "\n";
        
    }
    return 0;
}
