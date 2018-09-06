#include <iostream>

using namespace std;
int main(int argc, const char * argv[]) {
    int T, test_case;
    int M, N, x, y;
    int *Answer;
    int i, j;
    
    cin >> T;
    Answer = new int[T];
    
    for(test_case = 0; test_case < T; test_case++){
        cin >> M >> N >> x >> y;
        Answer[test_case] = -1;
        
        i = 0;
        j = 0;
        
        while(1){
            
            if(i*M+x == j*N+y) {Answer[test_case] = i*M+x; break;}
            else if(i*M+x > j*N+y) j++;
            else i++;
            if(i>N || j > M) break;
        }
    }
    
    for(test_case = 0; test_case < T; test_case++)
        cout << Answer[test_case] << endl;
    delete Answer;
    return 0;
}
