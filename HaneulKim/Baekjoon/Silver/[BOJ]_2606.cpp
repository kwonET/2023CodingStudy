#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, pair_cnt, t1, t2, cnt;
vector<int> graph[101];
int visitied[101];

void dfs(int r){
    if(visitied[r])
        return;
    visitied[r] = 1;
    cnt++;
    for(int i=0; i<graph[r].size(); i++){
        int tmp = graph[r][i];
        if(visitied[tmp] == 0){
            dfs(tmp);
        }
    }

}

int main(){

    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> pair_cnt;

    for(int i=0; i<pair_cnt; i++){
        cin >> t1 >> t2;
        graph[t1].push_back(t2);
        graph[t2].push_back(t1);
    }

    dfs(1);
    cout << cnt;


    
   
    return 0;

}