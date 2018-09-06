#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int T, test_case;
    unsigned int x, y;      //0 ≤ x < y < 2^31
    unsigned int dist;
    int i;
    int *a,b;   //b = ∑b
    
    cin >> T;
    
    a = new int[T];
    
    for(test_case = 0; test_case < T; test_case++){
        cin >> x >> y;
        dist = y - x;
        b = 0;
        i = 1;
        for(i = 1; dist>b; i++){
            b += (i+1)/2;
        }
        a[test_case] = i-1;
    }
    
    for(test_case = 0; test_case < T; test_case++)
        cout << a[test_case] << endl;
    
    delete a;
    return 0;
}
/*
dist 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17  ...
 a   1 2 3 3 4 4 5 5 5  6 6  6  7  7  7  8  8   ...

 i   1 2 3   4   5      6       7        8      ...
 b   1 1 2   2   3      3       4        4      ...
 */
//∑b(i) >= dist -> a = i
//ex)dist = 8 일때, ∑b(i->5) = 9 ≥ dist -> a = 5
