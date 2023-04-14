#include <iostream>

using namespace std;

int main(){
	int testcase = 0, st_num = 0, beyond = 0;;
	double total = 0, *avg, *score, *percent;
	int i = 0, j = 0;

	scanf("%d", &testcase);
	avg = new double[testcase];
	percent = new double[testcase];

	for(i = 0; i < testcase; i++){
		scanf("%d", &st_num);
		score = new double[st_num];
		for(j = 0; j < st_num; j++){
			scanf("%lf", score + j);
			total += score[j];
		}
		
		avg[i] = total/st_num;

		for(j = 0; j < st_num; j++){
			if(avg[i] < score[j])
				beyond++;
		}

		percent[i] = (double)beyond/st_num * 100;
		beyond = 0;
		total = 0;

		delete score;
	}

	
	for(i = 0; i < testcase; i++){
		printf("%.3lf%%\n", percent[i]);
	}
	return 0;
}