# import asyncio
# import logging
# from typing import Dict
#
#
# class Server:
#     def __init__(self, id: str, peers: Dict[str, str], data_dir: str):
#         self.logger = logging.getLogger(__name__)
#         self.id = id
#         self.peers = peers
#         self.data_dir = data_dir
#         self.queue = asyncio.Queue()
#         self.aserver = None
#         # self.loop=asyncio.new_event_loop()
#
#     async def _listen(self, listen_raft):
#         host, port = listen_raft.split(":")
#         self.logger.info(f"Starting server on {host}:{port}")
#         aserver = await asyncio.start_server(
#             self._tcp_receive, host, port
#         )  # , loop=self.loop)
#         addrs = ",".join(str(sock.getsockname()) for sock in aserver.sockets)
#         self.logger.info(f"Serving on {addrs}")
#         self.aserver = aserver
#
#     async def _tcp_receive(self, reader, writer):
#         # asyncio.create_task(self.queue.get())
#         data = await reader.read(100)
#         print(f"Decoded data {data.decode()}")
#
#     async def close(self):
#         if self.aserver:
#             self.aserver.close()
#             await self.aserver.wait_closed()
#
#     async def _serve_forever(self, listen_raft):
#         await self._listen(listen_raft)
#         async with self.aserver:
#             await self.aserver.serve_forever()
#
#     def serve(self, listen_raft):
#         asyncio.run(self._serve_forever(listen_raft))
#
#     # async def _prepare_server(self):
#     #     self.queue=asyncio.Queue()
#     #     server = await asyncio.start_server(handle_echo, '0.0.0.0', 8000)
#     #     addrs = ','.join(str(sock.getsockname()) for sock in server.sockets)
#     #     print(f"Serving on {addrs}")
#     #     async with server:
#     #         await server.serve_forever()
#     #
