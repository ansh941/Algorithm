#include <iostream>
using namespace std;

int main(){
	int month, day;
	int total_day = 0;

	cin >> month >> day;

	for(int i = 1; i < month; i++){
		switch(i){
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			total_day += 31;
			break;
		case 2:
			total_day += 28;
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			total_day += 30;
			break;
		}
	}

	total_day += day-1;

	switch(total_day % 7){
	case 0:
		cout << "MON\n";
		break;
	case 1:
		cout << "TUE\n";
		break;
	case 2:
		cout << "WED\n";
		break;
	case 3:
		cout << "THU\n";
		break;
	case 4:
		cout << "FRI\n";
		break;
	case 5:
		cout << "SAT\n";
		break;
	case 6:
		cout << "SUN\n";
		break;
	}

	return 0;
}