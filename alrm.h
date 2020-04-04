#include <time.h> // time_t, struct tm, difftime, time, mktime 

#ifndef _ALARMCOUNTDOWN_MAIN_H_
#define _ALARMCOUNTDOWN_MAIN_H_

struct tm * parse(struct tm * time, char* str);
char* format(time_t a, time_t b);

#endif // _ALARMCOUNTDOWN_MAIN_H_