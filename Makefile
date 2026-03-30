CC ?= cc
CFLAGS ?= -O2 -Wall -Wextra -std=c11
LDFLAGS ?=
LDLIBS ?= -libverbs

BIN := bin/min_rdma_tdx

.PHONY: all clean

all: $(BIN)

$(BIN): min_rdma_tdx.c
	mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -o $@ min_rdma_tdx.c $(LDFLAGS) $(LDLIBS)

clean:
	rm -rf bin
