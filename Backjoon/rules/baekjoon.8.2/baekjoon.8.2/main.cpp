#include <iostream>

using namespace std;

int main(){
    int num, i=0;
    int Answer;
    
    cin >> num;
    
    while(1){
        if(num>=1+6*(i-1)*i/2 && num <= 1+6*i*(i+1)/2){
            Answer = i+1;
            break;
        }
        i++;
    }
    
    cout << Answer << endl;
    
    return 0;
}
