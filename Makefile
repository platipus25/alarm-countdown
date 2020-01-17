CC=gcc
CFLAGS=-I -Wall

alarm-countdown: main.c
	$(CC) -o alarm-countdown main.c