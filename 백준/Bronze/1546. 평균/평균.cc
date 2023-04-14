#include <iostream>

using namespace std;

int main(){
	int exam = 0, i = 0;
	double total = 0.0, max = 0.0;
	double *score;

	scanf("%d", &exam);
	score = new double[exam];

	while(i < exam){
		scanf("%lf", score+i);
		if(score[i] > max)
			max = score[i];
		i++;
	}
	
	i = 0;

	while(i < exam){
		score[i] = score[i]/max * 100;
		total += score[i];
		i++;
	}

	printf("%.2lf", total/exam);
	return 0;
}