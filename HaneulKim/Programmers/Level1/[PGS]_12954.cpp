#include <string>
#include <vector>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    int change = x;
    while(n--){
        answer.push_back(change);
        change+=x;
    }
    return answer;
}