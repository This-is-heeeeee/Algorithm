#include <iostream>

using namespace std;

int buf;

int func(int n, int nums[]){
    int answer = 0;
    
    answer = buf = nums[0];
    
    for(int i = 1; i < n; i++){
        buf = (buf+nums[i] > nums[i]) ? (buf+nums[i]) : nums[i];
        if(answer < buf) answer = buf;
    }
    
    
    return answer;
}

int main(int argc, const char * argv[]) {
    int n;
    int nums[100000];
    
    cin >> n;
    
    for(int i = 0; i < n; i++)
        cin >> nums[i];
    
    cout << func(n,nums) << "\n";
    return 0;
}
