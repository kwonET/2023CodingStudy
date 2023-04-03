#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = false;
    int sum = 0, savex = x;
    while(x/10 > 0){
        sum += (x%10);
        x /= 10;
    }
    sum += (x%10);
    if(savex % sum == 0){
        answer = true;
    }
    else{
        answer = false;
    }
    return answer;
}