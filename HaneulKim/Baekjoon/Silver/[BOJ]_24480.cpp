#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, r, cnt;
int t1, t2;

vector<int> graph[100001];
int visitied[100001], result[100001];

void dfs(int r){
    if(visitied[r] == 1) return;
    
    visitied[r] = 1;
    cnt++;
    result[r] = cnt;

    for(int i=0; i<graph[r].size(); i++){
        dfs(graph[r][i]);
    }

}

int main(){

    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> m >> r;
    for(int i=0; i<m; i++){
        cin >> t1 >> t2;
        graph[t1].push_back(t2);
        graph[t2].push_back(t1);
    }

    for(int i=1; i<=n; i++){
        sort(graph[i].begin(), graph[i].end(), greater<>());
    }

    dfs(r);

    for(int i=1; i<=n; i++){
        cout << result[i] << '\n';
    }

        


    
   
    return 0;

}