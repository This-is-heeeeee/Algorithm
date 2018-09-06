#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    int stair[300] = {0,};
    int val[2][3];
    int Answer;
    cin >> N;
    
    for(int i = 0; i < N; i++){
        cin >> stair[i];
        if(i == 0){
            val[i%2][0] = stair[i];
            val[i%2][1] = stair[i];
            val[i%2][2] = 0;
        }
        else{
            val[i%2][0] = val[(i+1)%2][2] + stair[i];
            val[i%2][1] = val[(i+1)%2][0] + stair[i];
            val[i%2][2] = (val[(i+1)%2][0]>val[(i+1)%2][1]) ? val[(i+1)%2][0] : val[(i+1)%2][1];
        }
    }
    
    Answer = (val[(N-1)%2][0] > val[(N-1)%2][1]) ? val[(N-1)%2][0] : val[(N-1)%2][1];
    cout << Answer <<"\n";
    return 0;
}
