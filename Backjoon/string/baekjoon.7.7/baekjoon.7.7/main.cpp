#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int Answer = 0;
    int numA, numB, num;
    int i;
    
    cin >> numA;
    cin >> numB;
    /*
    for(i = 0; i < 3; i++){
        if(numA%10 > numB%10)
            num = numA;
        else if(numA%10 == numB%10){
            if(numA/10%10 > numB/10%10)
                num = numA;
            else if(numA/10%10 == numB/10%10){
                if(numA/100 > numB/100)
                    num = numA;
                else num = numB;
            }
            else num = numB;
        }
        else num = numB;
    }*/
    numA = numA/100 + numA/10%10*10 + numA%10*100;
    numB = numB/100 + numB/10%10*10 + numB%10*100;
    
    Answer = (numA > numB) ? numA:numB;
    cout << Answer << endl;
    return 0;
}
