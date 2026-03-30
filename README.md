# min_rdma_tdx

`genie(native)` server와 `simba(TDX guest)` client 사이에서 동작하는 최소 RDMA write checker다.

- server: native, `ibp23s0`
- client: TDX guest, `ibp1s0`
- bootstrap: TCP 1회만 사용
- data path: 이후 오직 `RDMA_WRITE`
- client buffer: `/dev/tdx_shmem`으로 shared 변환 후 MR 등록

## Files

- `min_rdma_tdx.c`: 단일 바이너리 구현
- `config/server_check.conf`: genie server
- `config/client_check.conf`: simba TDX guest client
- `config/server_bench.conf`
- `config/client_bench.conf`
- `run_td.py`: `../rdma_check/run_td.py` wrapper

## Build

```bash
make
```

## TDX Guest Bring-up

simba host에서:

```bash
sudo ./run_td.py --foreground
```

기본값은 `server_info.md` 기준으로 맞춰져 있다.

- RDMA NIC passthrough: `0000:6f:00.0`
- external SM

이 시나리오에서는 guest client가 `genie` 관리망으로 outbound TCP bootstrap을 거므로 추가 host forward가 필수는 아니다.

guest 안에서는 `/dev/tdx_shmem`이 준비돼 있어야 한다.

## Run

genie(native):

```bash
./bin/min_rdma_tdx config/server_check.conf
./bin/min_rdma_tdx config/server_bench.conf
```

simba(TDX guest):

```bash
./bin/min_rdma_tdx config/client_check.conf
./bin/min_rdma_tdx config/client_bench.conf
```

## Model

server는 `queue_depth * message_size` 크기의 지정 remote region을 미리 등록한다.
client는 bootstrap으로 받은 `addr/rkey`를 이용해 `slot = seq % queue_depth` 위치에만 `RDMA_WRITE` 한다.

현재 샘플 client config의 bootstrap 대상은 `10.20.26.87:7301`이다.
