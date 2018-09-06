#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main(int argc, const char * argv[]) {
    int T, test_case;
    int N, K;
    int rate[1000];
    int n1, n2;
    int idx;
    vector<int> vec[1000];
    stack<int> stc;
    int top, size, max = 0, buf = 0;
    
    cin >> T;
    for(test_case = 0; test_case<T; test_case++){
        cin >> N >> K;
        
        for(int i = 0; i < N; i++){
            cin >> rate[i];
        }
    
        for(int i = 0; i < K; i++){
            cin >> n1 >> n2;
            vec[n2-1].push_back(n1);
        }
        
        cin >> idx;
        
        stc.push(idx);
        
        while(1){
            top = stc.top();
            stc.pop();
            
            
            for(int i = 0; i < vec[top-1].size(); i++)
                stc.push(vec[top-1][i]);
            if(vec[top-1].empty())
                
        }
        
        
        
        cout << Answer <<"\n";
        Answer = 0;
    }
    return 0;
}
//DFS로 가장 큰 것.!
