#include <iostream>
#include <string.h>

using namespace std;

int buf[1001][1001] = {0,};

int func(string a, string b){
    for(int i = 0; i < a.length(); i++){
        for(int j = 0; j < b.length(); j++){
            if(a.at(i) == b.at(j)) buf[i+1][j+1] = buf[i][j]+1;
            else buf[i+1][j+1] = (buf[i+1][j] > buf[i][j+1]) ? buf[i+1][j] : buf[i][j+1];
        }
    }
    return buf[a.length()][b.length()];
}

int main(int argc, const char * argv[]) {
    string a, b;
    
    cin >> a >> b;
    
    cout << func(a,b) << "\n";
    return 0;
}
