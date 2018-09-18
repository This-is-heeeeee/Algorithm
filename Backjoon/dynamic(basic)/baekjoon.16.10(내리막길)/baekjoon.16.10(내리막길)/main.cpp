#include <iostream>
#include <string.h>

using namespace std;

int way[500][500] = {0,};

int func(int m, int n, int high[][500]){
    if(way[m][n] > -1) return way[m][n];
    
    way[m][n] = 0;
    
    if(m == 0 && n == 0) way[m][n] = 1;
    
    if(m-1 >= 0 && high[m][n] < high[m-1][n]){
        way[m][n] += func(m-1,n,high);
    }
    if(n-1 >= 0 && high[m][n] < high[m][n-1]){
        way[m][n] += func(m,n-1,high);
    }
    if(m+1 < 500 && high[m][n] < high[m+1][n]){
        way[m][n] += func(m+1,n,high);
    }
    if(n+1 < 500 && high[m][n] < high[m][n+1]){
        way[m][n] += func(m,n+1,high);
    }
    
    return way[m][n];
}

int main(int argc, const char * argv[]) {
    int M, N;
    int high[500][500] = {0,};
    
    cin >> M >> N;
    for(int i = 0; i < M; i++){
        for(int j = 0; j < N; j++){
            cin >> high[i][j];
        }
    }
    
    memset(way,-1,sizeof(way));
    
    cout << func(M-1,N-1,high) << "\n";
    return 0;
}
