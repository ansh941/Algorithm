#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> tmp;

    for(int count = 0; count < commands.size(); count++){
        int i = commands[count][0]-1;
        int j = commands[count][1];
        int k = commands[count][2]-1;
        
        tmp.assign(array.begin()+i, array.begin()+j);
        sort(tmp.begin(), tmp.end());
        answer.push_back(tmp.at(k));
        tmp.clear();
    }
    return answer;
}