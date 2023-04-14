#include <iostream>
#include <cstdio>

using namespace std;

int main(){
        int A = 0, B = 0, C = 0;
        int count[10] = {0};
        int mul;

        cin >> A;
        cin >> B;
        cin >> C;

        mul = A * B * C;

        while(mul){
                count[mul % 10]++;
                mul /= 10;
        }

        for(int i = 0; i < 10; i++)
                cout << count[i] << '\n';
        return 0;
}