#include <stdlib.h>		/* malloc */
#include <stdio.h>      /* printf, sprintf */
#include <time.h>       /* time_t, struct tm, difftime, time, mktime, asctime */

#include "alrm.h"


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

