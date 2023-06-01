#include <iostream>
#include <vector>
using namespace std;

int cnt;
int video_data[65][65];




void compression(int len, int row, int col){
    cnt = 0;
    for(int i=row; i<row+len; i++){
        for(int j=col; j<col+len; j++){
            if(video_data[i][j]) cnt++;  
        }
    }
    if(cnt == len*len){
        cout << "1";
        return ;
    }
    else if(cnt == 0){
        cout << "0";
        return ;
    }
    else{
        cout << '(';
        len /= 2;
        compression(len, row, col);
        compression(len, row, col+len);
        compression(len, row+len, col);
        compression(len, row+len, col+len);
        cout << ')';
        
        return ;
    }

}

int main(){

    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n;
    char tmp;
    cin >> n;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> tmp;
            video_data[i][j] = tmp - '0';
            if(tmp -'0') cnt++;
        }
    }

    if(cnt == n*n){
        cout << "1";
    }
    else if(cnt == 0){
        cout << "0";
    }
    else{
        int new_len = n/2;

        cout << '(';
        compression(new_len, 0, 0);
        compression(new_len, 0, new_len);
        compression(new_len, new_len, 0);
        compression(new_len, new_len, new_len);
        cout << ')';
    }
   
    return 0;

}