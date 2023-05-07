#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

    long long n, k;
    cin >> n >> k;
    k = min((long long)1000000000, k);
    long long cnt, ans = 0;
    long long low = 1;
    long long high = n*n;

    while(low <= high){
        cnt = 0;
        long long mid = (low + high)/2;
        for(int i=1; i<=n; i++){
            cnt += min(n, mid/i);
        }
        if(cnt >= k){
            ans = mid;
            high = mid - 1; 
        }
        else{
            low = mid + 1;
        }
    }
    cout << ans;

    return 0;
}