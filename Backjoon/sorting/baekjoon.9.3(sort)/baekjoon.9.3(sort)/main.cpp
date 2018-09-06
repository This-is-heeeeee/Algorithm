#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int num;
    int count[10000] = {0,};
    int N, i, k;
    
    cin >> N;
    
    for(i = 0; i < N; i++){
        cin >> num;
        count[num-1]++;
    }
    
    for(i = 0; i < 10000; i++){
        if(count[i]!=0)
            for(k = 0; k<count[i];k++)
                cout << i+1 << "\n";
    }
    
    return 0;
}
