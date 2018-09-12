#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    int val[1000][3] = {0,};
    int min;
    
    cin >> N;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < 3; j++){
            cin >> val[i][j];
            if(i > 0)
                val[i][j] += (val[i-1][(j+1)%3] < val[i-1][(j+2)%3]) ? val[i-1][(j+1)%3]:val[i-1][(j+2)%3];
        }
    }
    
    min = (val[N-1][0] < val[N-1][1]) ? val[N-1][0] : val[N-1][1];
    min = (min < val[N-1][2]) ? min : val[N-1][2];
    
    cout << min << "\n";
    return 0;
}
