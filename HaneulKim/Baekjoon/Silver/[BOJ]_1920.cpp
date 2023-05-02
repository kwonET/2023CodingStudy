#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    
    int n, m;
    cin >> n;
    vector<int> arr;
    int tmp;
    for(int i=0; i<n; i++){
        cin >> tmp;
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end());
    cin >> m;
    vector<int> find;
    for(int i=0; i<m; i++){
        cin >> tmp;
        find.push_back(tmp);
    }

    for(int i=0; i<m; i++){
        int left = 0; 
        int right = n-1; 
        int flag = 0;
        while(left <= right){ 
            int mid = (left + right)/2; 
            if(arr[mid] == find[i]){
                flag = 1;
                break;
            }
            else if(arr[mid] < find[i]){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        if(flag) cout << 1 << '\n';
        else cout << 0 << '\n';

    }



    return 0;
}

