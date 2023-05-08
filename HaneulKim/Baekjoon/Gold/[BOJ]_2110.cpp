#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){

    int n, c, num, start, end, install, ans = 0; // 집 개수, 공유기 개수
    cin >> n >> c;
    vector<int> x;
    for(int i=0; i<n; i++){
        cin >> num;
        x.push_back(num);
    } 
    sort(x.begin(), x.end());

    start = 1;
    end = x[n-1] - x[0];

    while(start <= end){
        install = 1;
        int mid = (start + end)/2;
        int st  = x[0];
        for(int i=1; i<n; i++){
            if(x[i] - st >= mid){
                install++;
                st = x[i];
            }
        }
        if(install >= c){
            ans = max(ans, mid);
            start = mid + 1; 
        }
        else{
            end = mid - 1;
        }
    }
    cout << ans;



    return 0;
}