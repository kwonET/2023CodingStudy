#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    vector<int> copy;
    if(arr.size() == 1) answer.push_back(-1);
    else{
        for(int i=0; i<arr.size(); i++){
            copy.push_back(arr[i]); 
        }
        sort(copy.begin(), copy.end());
        int min = copy[0];
        for(int i=0; i<arr.size(); i++){
            if(arr[i] == min){
                arr.erase(arr.begin() + i);
                break;
            }
        }
        for(int i=0; i<arr.size(); i++)
            answer.push_back(arr[i]);
    }
    
    
    return answer;
}