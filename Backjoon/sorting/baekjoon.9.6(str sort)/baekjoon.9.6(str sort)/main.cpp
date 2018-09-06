#include <iostream>
#include <string>

using namespace std;

void sorting(string *str, int first, int last){
    int index1 = first;
    int index2 = last;
    string temp;
    
    if(first >= last) return;
    
    while(index1 <= index2){
        while(str[index1].length() < str[first].length() && index1 < index2 ) index1++;
        while(str[index2].length() > str[first].length() && index1 <= index2) index2--;
        if(str[index1].length() == str[first].length() && str[index1] <= str[first]){ index1++; continue;}
        if(str[index2].length() == str[first].length() && str[index2] > str[first]){ index2--; continue;}
        
        if(index1 < index2){
            temp = str[index1];
            str[index1] = str[index2];
            str[index2] = temp;
        }
        else break;
    }
    
    temp = str[first];
    str[first] = str[index2];
    str[index2] = temp;
    
    sorting(str, first, index2-1);
    sorting(str, index2+1, last);
    
    return;
}

int main(int argc, const char * argv[]) {

    int N;
    string *str;
    string *fin;
    
    cin >> N;
    
    str = new string[N];
    fin = new string[N];
    
    for(int i = 0; i < N; i++)
        cin >> str[i];
    
    sorting(str, 0, N-1);
    
    int k = 0;
    for(int i = 0; i < N; i++){
        if(i<N-1 && str[i] == str[i+1]) continue;
        fin[k] = str[i];
        k++;
    }
    
    for(int i = 0; i < k; i++)
        cout << fin[i] <<"\n";
    
    delete []str;
    delete []fin;
    return 0;
}
