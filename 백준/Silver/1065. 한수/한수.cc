#include <iostream>

using namespace std;

int main(){
	int max = 0;
	int temp[3] = {0};
	int gap = 0;
	int count = 99;

	cin >> max;

	if(max <= count)
		count = max;
	else{
		for(int i = 100; i <= max; i++){
			temp[0] = i / 100;
			temp[1] = (i % 100) / 10;
			temp[2] = i % 10;

			if((temp [0] - temp[1]) == (temp[1] - temp[2])){
				count++;
			}
		}
	}

	cout << count << "\n";
	return 0;
}