#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, const char * argv[]) {
    int Answer = 0;
    int i;
    string s;
    
    getline(cin, s, '\n');
    
    for(i = 0; i < s.size(); i++){
        if(s.at(i) != ' ')
            if(i + 1 >= s.size() || s.at(i+1) == ' '){
                Answer++;
            }
    }
    
    cout << Answer << endl;
    return 0;
}
