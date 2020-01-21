#include <stdlib.h>		/* malloc */
#include <stdio.h>      /* printf, sprintf */
#include <time.h>       /* time_t, struct tm, difftime, time, mktime, asctime */
#include <stdbool.h>	/* bool, true, false */
#include <string.h>     /* strcmp */

#include <unistd.h>		/* sleep */

#include "main.h"

int main (int argc, char* argv[]) {
	time_t now;
	struct tm* morning;
	bool loop = false;
	char* input = (char*)malloc(10 * sizeof(char));;

	// parse args:

	for(int i = 0; i < argc; i++){
		char* v = argv[i];
		if(strcmp(v, "-u") == 0 || strcmp(v, "-U") == 0){
			loop = true;
		}else if (i > 0){
			strcpy(input, v);
		}
	}

	if(strlen(input) < 1){
		printf("Input a date: ");
		scanf("%s", input);
	}


	time(&now);  /* get current time; same as: timer = time(NULL)  */
	
	morning = localtime(&now);
	morning->tm_sec = 0;

	parse(morning, input);

	if(mktime(morning) < now){
		morning->tm_mday++;
	}

	if(loop){
		printf("%s", asctime(morning));
	}
	while(true) {
		time(&now);
		char* formatted = format(mktime(morning), now);

		printf("%s", formatted);

		if(!loop){
			printf(" until %s", asctime(morning));
			break;
		}

		printf("\r");
		fflush(stdout);
		sleep(1);
	};
	

	return 0;
}

struct tm* parse(struct tm* time, char* str){
	int hours = 0;
	int minutes = 0;

	sscanf(str, "%d:%d", &hours, &minutes);

	time->tm_hour = hours;
	time->tm_min = minutes;
	
	return time;
}

char* format(time_t a, time_t b){
	char* out = (char*)malloc(20 * sizeof(char));
	int hours = 0;
	int minutes = 0;
	int seconds = 0;
	int diff = difftime(a, b);

	seconds = diff % 60;

	diff = diff / 60; // diff now represents minutes

	minutes = diff % 60;
	
	diff = diff / 60; // diff now represents hours

	hours = diff;

	sprintf(out, "%d:%02d:%02d", hours, minutes, seconds);
	return out;
}