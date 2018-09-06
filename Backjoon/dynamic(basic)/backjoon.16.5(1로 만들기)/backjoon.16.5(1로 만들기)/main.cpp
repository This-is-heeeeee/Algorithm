#include <iostream>
#include <queue>

using namespace std;
bool visit[1000000];

int main(int argc, const char * argv[]) {
    int N;
    queue<int> que;
    int Answer = 0;
    int size;
    
    cin >> N;
    
    fill_n(visit,N,false);
    
    que.push(N);
    
    while(1){
        size = (int)que.size();
        for(int i = 0; i < size; i++){
            if(!visit[que.front()-1]){
                if(que.front() == 1){
                    cout << Answer <<"\n";
                    return 0;
                }
                visit[que.front()-1] = true;
                if(que.front()%3 == 0) que.push(que.front()/3);
                if(que.front()%2 == 0) que.push(que.front()/2);
                que.push(que.front()-1);
            }
            que.pop();
        }
        Answer++;
    }
    return 0;
}
