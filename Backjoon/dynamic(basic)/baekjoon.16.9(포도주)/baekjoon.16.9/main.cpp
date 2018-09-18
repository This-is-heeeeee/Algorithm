#include <iostream>

using namespace std;

int func(int n, unsigned int arr[][3]){
    int answer = 0;
    
    arr[0][1] = arr[0][0];
    arr[0][2] = 0;
    
    for(int i = 1; i < n; i++){
        arr[i][2] = (arr[i-1][0] > arr[i-1][1]) ? arr[i-1][0] : arr[i-1][1];
        arr[i][2] = (arr[i][2] > arr[i-1][2]) ? arr[i][2] : arr[i-1][2];
        arr[i][1] = arr[i-1][0] + arr[i][0];
        arr[i][0] += arr[i-1][2];
    }
    
    answer = (arr[n-1][0] > arr[n-1][1]) ? arr[n-1][0] : arr[n-1][1];
    answer = (answer > arr[n-1][2]) ? answer : arr[n-1][2];
    
    return answer;
}

int main(int argc, const char * argv[]) {
    int n;
    unsigned int wine[10000][3] = {0,};
    
    cin >> n;
    
    for(int i = 0; i < n; i++){
        cin >> wine[i][0];
    }
    
    cout << func(n,wine) << "\n";
    return 0;
}
