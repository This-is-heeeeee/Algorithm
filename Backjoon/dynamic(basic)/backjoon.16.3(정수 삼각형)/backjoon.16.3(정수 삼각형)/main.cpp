#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    int val[500][500] = {0,};
    int max = 0;
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j <= i; j++){
            cin >> val[i][j];
            if(i > 0){
                if(j == 0) val[i][j] += val[i-1][j];
                else if(j == i) val[i][j] += val[i-1][j-1];
                else val[i][j] += (val[i-1][j-1] > val[i-1][j]) ? val[i-1][j-1] : val[i-1][j];
            }
        }
    }
    
    for(int i = 0; i < N; i++){
        if(max < val[N-1][i]) max = val[N-1][i];
    }
    
    cout << max <<"\n";
    return 0;
}
