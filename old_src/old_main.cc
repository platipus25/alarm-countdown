#include <stdlib.h>		/* malloc */
#include <stdio.h>      /* printf, sprintf */
#include <time.h>       /* time_t, struct tm, difftime, time, mktime, asctime */
#include <stdbool.h>	/* bool, true, false */
#include <string.h>     /* strcmp */

#include <unistd.h>		/* sleep */

#include "alrm.h"

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


	time(&now);  /* get current time; same as: now = time(NULL)  */
	
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
