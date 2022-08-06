# import asyncio
# import logging
# import logging.config
#
# import pytest
#
# from tests.conftest import config
#
# logger = logging.getLogger(__name__)
# # @pytest.mark.asyncio
# # async def test_serve(test_raft_server, config):
# #     server = test_raft_server
# #     #client_reader, client_writer = test_raft_reader_writer
# #     # client_writer.write(b"hello")
# #     # assert client_reader.read(5) == b"hello"
# #     # client_reader.close()
# #     # client_writer.close()
# #     listen_raft = config["listen_raft"]
# #     assert server.aserver is not None
#
#
# @pytest.mark.asyncio
# async def test_client(test_raft_server, test_raft_reader_writer):
#     client_reader, client_writer = test_raft_reader_writer
#     logger.info("Sending hello")
#     client_writer.write("hello".encode())
#     await client_writer.drain()
#     # data = await client_reader.read(100)
#     client_writer.close()
#     # assert data.decode() == "hello"
