#include <iostream>
using namespace std;

int main(){
	int num = 0;

	cin >> num;

	for(int i = 0; i < num; i++){

		for(int j = i; j < num ; j++){
			cout << "*";
		}
		cout << "\n";
	}

	return 0;
}