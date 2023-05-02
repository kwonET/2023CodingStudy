#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    
    ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

    int n, m, tmp;
    cin >> n;
    vector<int> arr;
    for(int i=0; i<n; i++){
        cin >> tmp;
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end());
    cin >> m;
    
    int sum, result;
    int left = 0;
    int right = arr[n-1];
    while(left <= right){
        sum = 0;
        int mid = (left + right)/2;
        for(int i=0; i<n; i++){
            sum += min(arr[i], mid);
        }
        if(sum <= m){
            result = mid;
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
    cout << result;
    

    return 0;
}
