#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    int N, M, V;
    int p1, p2, v1, v2;
    vector<int> *vec;
    queue<int> que;
    stack<int> stc;
    bool visit[1000] = {false, };
    
    cin >> N >> M >> V;
    
    vec = new vector<int>[N];
    
    for(int i = 0; i < M; i++){
        cin >> p1 >> p2;
        
        //v1 = (p1<p2) ? p1:p2;
        //v2 = (p1>p2) ? p1:p2;
        
        //vec[v1-1].push_back(v2);
        vec[p1-1].push_back(p2);
        vec[p2-1].push_back(p1);
    }
    for(int i = 0; i < N; i++){
        sort(vec[i].begin(),vec[i].end());
    }
    //DFS
    stc.push(V);
    while(!stc.empty()){
        int top = stc.top();
        stc.pop();
        if(!visit[top-1]){
            cout << top << " ";
            visit[top-1] = true;
            for(int i = 0; i < (int)vec[top-1].size(); i++){
                if(!visit[vec[top-1][(vec[top-1].size()-1)-i]-1]){
                    stc.push(vec[top-1][vec[top-1].size()-1-i]);
                }
            }
        }
    }
    cout << "\n";
    //BFS
    for(int i = 0; i < N; i++)
        visit[i] = false;
    que.push(V);
    visit[V-1] = true;
    while(!que.empty()){
        cout << que.front() << " ";
        for(int i = 0; i < vec[que.front()-1].size(); i++){
            if(!visit[vec[que.front()-1][i]-1]){
                que.push(vec[que.front()-1][i]);
                visit[vec[que.front()-1][i]-1] = true;
            }
        }
        que.pop();
    }
    cout << "\n";
    return 0;
}
