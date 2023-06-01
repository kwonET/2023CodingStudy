#include <iostream>
#include <string>
#include <vector>

using namespace std;

int a_pos, b_pos, ans_pos;

int main(){

    ios_base::sync_with_stdio(0); 
    cin.tie(0); 
    cout.tie(0);

    int n, m, tmp;
    cin >> n >> m;
    vector<int> A, B;

    for(int i=0; i<n; i++){
        cin >> tmp;
        A.push_back(tmp);    
    }
    for(int i=0; i<m; i++){
        cin >> tmp;
        B.push_back(tmp);    
    }
    
    while(a_pos < A.size() && b_pos < B.size()){
        if(A[a_pos] < B[b_pos]){
            cout << A[a_pos++] << ' ';
        }
        else{
            cout << B[b_pos++] << ' ';
        }
    }
    while(a_pos < A.size()){
        cout << A[a_pos++] << ' ';
    }
    while(b_pos < B.size()){
        cout << B[b_pos++] << ' ';
    }
    



    return 0;
}