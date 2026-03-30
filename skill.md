server node는 native 환경에서 운영됨.

client node는 tdx 환경에서 운영됨.

server 와 client는 물리적으로 다른 서버에서 운영됨.

server는 genie(native)에서, client는 simba(tdx)에서 운영됨.

rdma_check의 기능을 그대로 구현하되, 그 운영을 위와 같은 서버에 맞게 수정하는 것이 목표.

reference repository는 총 2개가 존재함.
rdma 통신은 rdma_check dir을, tdx 내에서 client측이 private memory를 shared로 바꾸는 것은 share dir를 참고할 수 있도록

tcp는 bootstrap 단계에서만 이용될 것이며, 한번 initialized 된 이후에는 오로지 rdma만 이용할 수 있도록.

rdma_check/run_td.py는 simba에서 tdx vm을 열기 위해서 사용되는 qemu instruction py인데, 만약 잘못된 내용이 있으면 같이 수정할 수 있도록