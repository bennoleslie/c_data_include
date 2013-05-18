all: test

foo.c: foo.html
	./bin2c.py $<

test: test.c foo.c
	gcc test.c foo.c -o $@
