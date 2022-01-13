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

string func2(string a, string b){
    string answer = "";
    int length;
    int i = a.length();
    int j = b.length();
    length = buf[i][j];
    
    while(length != 0){
        if(buf[i-1][j]+1 == length && buf[i][j-1]+1 == length){
            answer = a.at(i-1) + answer;
            length -= 1;
            i-=1;j-=1;
        }
        else if(buf[i-1][j] == length && buf[i][j-1] < length)
            i -= 1;
        else
            j -= 1;
    }
    
    return answer;
}

int main(int argc, const char * argv[]) {
    string a, b;
    
    cin >> a >> b;
    
    cout << func(a,b) << "\n";
    cout << func2(a,b) << "\n";
    return 0;
}
