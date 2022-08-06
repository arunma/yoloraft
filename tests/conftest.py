import sys
from pathlib import Path

import pytest
import yaml
from _pytest.monkeypatch import MonkeyPatch

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
    monkeypatch.chdir(base_path)
    config_file = open("../clusters/a/conf.yaml")
    config = yaml.safe_load(config_file)
    return config
