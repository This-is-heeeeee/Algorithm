#include <iostream>

using namespace std;

long arr[100][10] = {0,1,1,1,1,1,1,1,1,1,};

int main(int argc, const char * argv[]) {
    int N;
    long Answer = 0;
    
    cin >> N;
    
    for(int i = 1; i < N; i++){
        for(int j = 0; j < 10; j++){
            if(j == 0)
                arr[i][j] = arr[i-1][j+1];
            else if(j == 9)
                arr[i][j] = arr[i-1][j-1];
            else
                arr[i][j] = (arr[i-1][j-1] + arr[i-1][j+1])%1000000000;
        }
    }
    
    for(int i = 0; i < 10; i++)
        Answer += arr[N-1][i];
    Answer %= 1000000000;
    
    cout << Answer << "\n";
    return 0;
}
