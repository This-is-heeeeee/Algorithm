#include <iostream>

using namespace std;

int count_2 = 0;
int count_5 = 0;

void func(int i){
    if(i > 1)
    {
        func(i-1);
        while(i % 5 == 0){
            i/=5;
            count_5++;
        }
        while(i % 2 == 0){
            i/=2;
            count_2++;
        }
    }
}

int main(int argc, const char * argv[]) {
    int num;
    int count = 0;
    
    cin >> num;
    
    func(num);
    
    count = (count_2 < count_5) ? count_2 : count_5;
    
    cout << count <<"\n";
    return 0;
}
