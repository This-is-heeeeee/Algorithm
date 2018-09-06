#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int T,N;
    long count0_0 = 0, count1_0 = 1;
    long count0_1 = 1, count1_1 = 1;
    long count0, count1;
    
    cin >> T;
    
    for(int test_case = 0; test_case < T; test_case++){
        cin >> N;
        
        for(int i = 0; i < N-2; i++){
            if(count0_0 <= count0_1)
                count0_0 = count0_0 + count0_1;
            else
                count0_1 = count0_0 + count0_1;
            if(count1_0 <= count1_1)
                count1_0 = count1_0 + count1_1;
            else
                count1_1 = count1_0 + count1_1;
        }
        
        count0 = (count0_0 > count0_1) ? count0_0 : count0_1;
        count1 = (count1_0 > count1_1) ? count1_0 : count1_1;
        
        if(N == 0) count1 = 0;
        else if(N == 1) count0 = 0;
        
        cout << count0 << " " << count1 << "\n";
        
        count0_0 = 0;
        count0_1 = 1;
        count1_0 = 1;
        count1_1 = 1;
    }
    return 0;
}
