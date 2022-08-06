# from dataclasses import dataclass
# from typing import *
#
#
# @dataclass(unsafe_hash=True)
# class Log:
#     def __init__(self, store: Store):
#         self.store=store
#         switch if store.committed()==0:
#
#         self.last_index=0
#
#
# class Server:
#     def __init__(self, id: str, peers: Dict[str, str], data_dir: str):
#         self.id = id
#         self.peers = peers
#         self.data_dir = data_dir
#         self.raft_server = RaftServer(self.id, self.peers, self.data_dir)
#         self.kv_server = KVServer(self.id, self.peers, self.data_dir)
#         self.cluster_manager_server = ClusterManagerServer(self.id, self.peers, self.data_dir)
#
#     def serve(self, listen_raft):
#         asyncio.run(self.raft_server.start(listen_raft))
#         asyncio.run(self.kv_server.start())
#         asyncio.run(self.cluster_manager_server.start())
