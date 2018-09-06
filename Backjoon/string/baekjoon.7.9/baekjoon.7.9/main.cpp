//
//  main.cpp
//  baekjoon.7.9
//
//  Created by LeeGN on 2018. 7. 23..
//  Copyright © 2018년 LeeGN. All rights reserved.
//

#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, const char * argv[]) {
    
    char *croatia[] = {"c=", "c-", "d-", "lj", "nj", "s=", "z=", "dz="};
    char s[100];
    int i, j, n, len;
    int Answer = 0;
    
    cin >> s;
    n = strlen(s);
    
    for(i = 0; i < n; i++){
        for(j = 0; j<8;j++) {
            len = strlen(croatia[j]);
            if(strncmp(s + i, croatia[j],len) == 0){
                i += (len-1);
                break;
            }
        }
        Answer++;
    }
    cout << Answer << endl;
    return 0;
}
