//
//  main.cpp
//  baekjoon.7.8
//
//  Created by LeeGN on 2018. 7. 23..
//  Copyright © 2018년 LeeGN. All rights reserved.
//

#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, const char * argv[]) {
    
    char s[15];
    int i, n;
    int Answer = 0;
    
    cin >> s;
    
    n = strlen(s);
    
    for(i = 0; i < n; i ++){
        switch(s[i]){
            case 'A':
            case 'B':
            case 'C':
                Answer += 3;
                break;
            case 'D':
            case 'E':
            case 'F':
                Answer +=4;
                break;
            case 'G':
            case 'H':
            case 'I':
                Answer += 5;
                break;
            case 'J':
            case 'K':
            case 'L':
                Answer +=6;
                break;
            case 'M':
            case 'N':
            case 'O':
                Answer +=7;
                break;
            case 'P':
            case 'Q':
            case 'R':
            case 'S':
                Answer += 8;
                break;
            case 'T':
            case 'U':
            case 'V':
                Answer += 9;
                break;
            case 'W':
            case 'X':
            case 'Y':
            case 'Z':
                Answer += 10;
                break;
        }
        
    }
    
    std::cout << Answer << endl;
    return 0;
}
