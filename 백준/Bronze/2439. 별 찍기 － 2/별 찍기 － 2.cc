#include <iostream>
using namespace std;

int main(){
	int num = 0;

	cin >> num;

	for(int i = 0; i < num; i++){

		for(int j = i+1; j < num ; j++){
			cout << " ";
		}
		for(int j = 0; j <= i; j++){
			cout << "*";
		}
		cout << "\n";
	}

	return 0;
}