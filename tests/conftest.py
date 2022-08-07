import asyncio
import logging
import pathlib
from pathlib import Path

import pytest
import pytest_asyncio
import yaml
from _pytest.monkeypatch import MonkeyPatch

from yoloraft.config import ConfigLoader

# from yoloraft.raft.server import Server
import logging.config

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def pytest_sessionstart(session):
    logging.basicConfig(
        format="%(asctime)s : %(levelname)s : %(message)s",
        level=logging.INFO,
        filename="ex.log",
    )


@pytest.fixture(scope="module")
def monkeypatch():
    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.fixture(scope="module")
def base_path() -> Path:
    return Path(__file__).parent


@pytest.fixture(scope="module")
def config(base_path, monkeypatch):
    logger.info("Constructing config")
    monkeypatch.chdir(base_path)
    config_path = pathlib.Path("../clusters/a/conf.yaml")
    config = ConfigLoader.load(config_path)
    return config


# @pytest_asyncio.fixture
# async def test_raft_server(config):
#     logger.info("Constructing server")
#     server = Server(config.id, config.peers, config.data_dir)
#     yield await server._listen(config.listen_raft)
#     await server.close()
#
#
# @pytest_asyncio.fixture
# async def test_raft_reader_writer(config):
#     listen_raft = config.listen_raft
#     host, port = listen_raft.split(":")
#     client_reader, client_writer = await asyncio.open_connection(host, port)
#     return client_reader, client_writer
