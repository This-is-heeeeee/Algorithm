#include <iostream>

using namespace std;
void sorting(int *sort, int *temp, int first, int last);

int main(int argc, const char * argv[]) {
    int N;
    int *sort;
    int *temp;
    
    cin >> N;
    
    sort = new int[N];
    temp = new int[N];
    
    for(int i = 0; i < N; i++)
        cin >> sort[i];
    
    sorting(sort, temp, 0, N-1);
    
    for(int i = 0; i < N; i++)
        cout << sort[i] << "\n";
    
    delete sort;
    delete temp;
    return 0;
}

void sorting(int *sort, int *temp, int first, int last){
    if(first>=last) return;
    
    int mid = (first + last)/2;
    int index = first;
    int index1 = first;
    int index2 = mid + 1;
    
    sorting(sort, temp, first, mid);
    sorting(sort, temp, mid+1, last);
    
    while(index1 <= mid && index2 <= last){
        if(sort[index1] > sort[index2]) temp[index++] = sort[index2++];
        else temp[index++] = sort[index1++];
    }
    
    while(index1<=mid) temp[index++] = sort[index1++];
    while(index2<=last) temp[index++] = sort[index2++];
    
    for(int i = first; i <= last; i++)
        sort[i] = temp[i];
    return;
}
