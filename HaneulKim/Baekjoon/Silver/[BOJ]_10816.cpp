#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


int fuc(long long * arr, int n, long long x){
	int left = 0;
	int right = n-1;
	while(left<right){
		int mid = (left + right)/2;
		if(arr[mid]<x){
			left = mid + 1;
		}
		else{
			right = mid;
		}
	}
	if(arr[left] == x) return left;
	else return -1;
}

int fuc2(long long * arr, int n, long long x){
	int left = 0;
	int right = n-1;
	while(left<right){
		int mid = (left + right+1)/2;
		if(arr[mid]<=x){
			left = mid;
		}
		else{
			right = mid-1;
		}
	}
	if(arr[left] == x) return left;
	else return -1;
}


int main(){
	
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	
	int n;
	cin >> n;
	
	long long arr[n] = {0,};
	
	for(int i=0; i<n; i++){
		long long tmp;
		cin >> tmp;
		arr[i] = tmp;
	}
	
	sort(arr, arr+n);
	
	
	int m;
	cin >> m;
	
	long long ans, ans2;
	
	for(int i=0; i<m; i++){
		long long tmp;
		cin >> tmp;
		ans = fuc(arr, n, tmp);
		ans2 = fuc2(arr, n, tmp);
		if(ans == -1) cout << "0 ";
		else{
			cout << ans2-ans+1 << ' ';
		}
		
	}
	
	
	
}
