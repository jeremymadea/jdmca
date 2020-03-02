CC=gcc 
CFLAGS=-Wall -I/opt/local/include -L/opt/local/lib -I/Users/jeremy/include -L/Users/jeremy/lib
LIBS=-lgd -lm

all: jdmca

jdmca: ca1d.o jdmca.o makegif.o fillrow.o
	$(CC) $(CFLAGS) ca1d.o jdmca.o makegif.o fillrow.o -o jdmca $(LIBS)

jdmca.cgi: ca1d.o jdmca_cgi.o makegif.o fillrow.o
	$(CC) $(CFLAGS) ca1d.o jdmca_cgi.o makegif.o fillrow.o -o jdmca.cgi $(LIBS) -lcgic

fillrow.o: fillrow.c fillrow.h
makegif.o: makegif.c makegif.h
ca1d.o: ca1d.c ca1d.h
jdmca.o: jdmca.c ca1d.h makegif.h fillrow.h
jdmca_cgi.o: jdmca_cgi.c ca1d.h makegif.h fillrow.h

clean:
	rm -f *.o jdmca 


