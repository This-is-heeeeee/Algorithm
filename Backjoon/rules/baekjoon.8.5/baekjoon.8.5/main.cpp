#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int T, test_case;
    int H, W, N;
    int *room;
    
    cin >> T;
    
    room = new int[T];
    
    for(test_case = 0; test_case < T; test_case++){
        cin >> H >> W >> N;
        
        if(N%H > 0)
            room[test_case] = N%H*100 + N/H+1;
        
        else
            room[test_case] = H*100 + N/H;
    }
    
    for(test_case = 0; test_case < T; test_case++)
        cout << room[test_case] << endl;
    
    delete room;
    
    return 0;
}
