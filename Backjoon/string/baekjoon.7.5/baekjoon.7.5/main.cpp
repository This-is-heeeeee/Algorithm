#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    
    int Answer = 0;
    int N, i, len, j, buf, k;
    char word[100];
    char alphabet[26];
    
    
    cin >> N;
    
    for(i = 0; i < N; i++){
        cin >>word;
        len = strlen(word);
        buf = 0;
        for(j = 0;j < len;j++){
            if(word[j] != word[j+1]){
                alphabet[buf] = word[j];
                buf++;
            }
        }
        bool check = false;
        for(j = 0; j < buf; j++)
            for(k = j+1; k < buf; k++)
                if(alphabet[j] == alphabet[k])
                    check = true;
        
        if(!check)
            Answer++;
    }
    
    cout << Answer << endl;
    return 0;
}
