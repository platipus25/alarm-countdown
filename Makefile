CC=gcc
CFLAGS=-I -Wall
DEPS := alrm.h
OBJ := main.o alrm.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

alarm-countdown: $(OBJ)
	$(CC) -o $@ $^
