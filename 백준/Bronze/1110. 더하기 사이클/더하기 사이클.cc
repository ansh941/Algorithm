#include <iostream>

using namespace std;

int main(){
	int num = 0, first = 0, count = 1;

	cin >> num;
	first = num;

	do{
		num = ( (num % 10) * 10 ) + ( ( (num / 10) + (num  % 10) ) % 10);
		count++;
	}while(num != first);

	cout << count-1 << "\n";
	return 0;
}