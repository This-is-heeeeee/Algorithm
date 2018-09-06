#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    int num[10] = {0,};
    int room;
    
    cin >> room;
    
    while(1){
        num[room%10]++;
        room/=10;
        if(room == 0) break;
    }
    
    if((num[6] + num[9])%2 == 0)
        num[6] = (num[6] + num[9])/2;
    else
        num[6] = (num[6] + num[9])/2+1;
    /*
    int max = 0;
    for(int i = 0; i < 9; i++)
        if(max < num[i])
            max = num[i];
     */
    sort(num,num+9);
    
    cout << num[8] << endl;
    return 0;
}
