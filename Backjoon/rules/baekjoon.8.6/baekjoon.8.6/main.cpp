#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    string day[] = {"SUN","MON","TUE", "WED","THU","FRI","SAT"};
    int month,date;
    int calc = 0;
    
    cin >> month >> date;
    
    calc = (month-1)*31;
    
    if(month > 4) calc -= 1;
    if(month > 6) calc -= 1;
    if(month > 9) calc -= 1;
    if(month > 11) calc -= 1;
    if(month > 2) calc -= 3;
    
    calc += date;
    
    std::cout << day[calc%7] << endl;
    return 0;
}
