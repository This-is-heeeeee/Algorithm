#include <iostream>
#include <string>

using namespace std;

struct Fibo{
    unsigned long long f[2][2] = {{1,1},{1,0}};
};

Fibo multiply(Fibo A, Fibo B){
    Fibo M;
    
    M.f[0][0] = (A.f[0][0] * B.f[0][0] + A.f[0][1] * B.f[1][0])%1000000;
    M.f[0][1] = (A.f[0][0] * B.f[0][1] + A.f[0][1] * B.f[1][1])%1000000;
    M.f[1][0] = (A.f[1][0] * B.f[0][0] + A.f[1][1] * B.f[1][0])%1000000;
    M.f[1][1] = (A.f[1][0] * B.f[0][1] + A.f[1][1] * B.f[1][1])%1000000;
    
    return M;
}

Fibo Matrix(Fibo M, unsigned long long n){
    if(n>1){
        M = Matrix(M, n/2);
        M = multiply(M,M);
        if(n&1){
            Fibo F1;
            M = multiply(M,F1);
        }
    }
    return M;
}

int main(int argc, const char * argv[]) {
    unsigned long long N;
    
    cin >> N;
    
    Fibo M;
    
    M = Matrix(M,N);
    
    cout << M.f[0][1] << "\n";
    return 0;
}
