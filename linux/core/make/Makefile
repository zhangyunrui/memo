all: test

test: test.o anotherTest.o
	gcc -Wall test.o anotherTest.o -o test

test.o: test.c
	gcc -c -Wall test.c

anotherTest.o: anotherTest.c
	gcc -c -Wall anotherTest.c

clean:
	rm -rf *.o test
