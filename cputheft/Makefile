DIRS := $(wildcard ????.??)
TARS := $(DIRS:%=%.tar.gz)

all: $(TARS)

%.tar.gz:%
	tar zcvf $@ $<

clean:
	rm -f *.tar.gz
