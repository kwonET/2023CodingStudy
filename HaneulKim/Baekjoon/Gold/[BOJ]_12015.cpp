#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

    int N, num, tmp, st = 0;
    cin >> N;
    vector<int> arr, ans;
    for(int i=0; i<N; i++){
        cin >> num;
        arr.push_back(num);
    }
    arr.resize(N+1);
    ans.push_back(arr[0]);
    int cnt = 1;
    for(int i=1; i<N; i++){
        if(ans.back() < arr[i]){
            ans.push_back(arr[i]);
            st++;
            cnt++;
        }
        else{
            int pos, left, right;
            left = 0;
            right = ans.size()-1;
            while(left <= right){
                int mid = (left + right)/2;
                if(arr[i] > ans[mid]){
                    left = mid + 1;
                }
                else{
                    pos = mid;
                    right = mid - 1;
                }
                
            }
            ans[pos] = arr[i];
        }
    }

    cout << cnt;




    return 0;
}