KEY:=ffffffffffffffff
.PHONY: all key.h

all: solveme_alt.cpp key.h
	g++ -std=c++0x solveme_alt.cpp -ftemplate-depth-1000000 -o solveme

key.h: 
#	echo '${KEY}' | perl -p -e 's/(.)/sprintf("K(%d,%d)\n",$$i++,ord($$1))/ge' > key.h
