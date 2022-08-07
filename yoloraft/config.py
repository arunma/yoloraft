import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

import yaml


@dataclass(unsafe_hash=True)
class Config:
    cluster_name: str
    id: str
    data_dir: str
    listen_raft: str
    peers: Dict[str, str]
    election_timeout_min: int
    election_timeout_max: int
    heartbeat_interval: int
    # Let's see if we can implement this
    max_payload_entries: int
    replication_lag_threshold: int
    snapshot_policy: Dict[str, str]

    def new_random_election_timeout(self):
        return random.randint(self.election_timeout_min, self.election_timeout_max)


class ConfigLoader:
    @classmethod
    def load(cls, path: Path) -> Config:
        with open(path, "r") as file:
            config = yaml.safe_load(file)
            return Config(
                config["cluster_name"],
                config["id"],
                config["data_dir"],
                config["listen_raft"],
                config["peers"],
                config["election_timeout_min"],
                config["election_timeout_max"],
                config["heartbeat_interval"],
                config["max_payload_entries"],
                config["replication_lag_threshold"],
                config["snapshot_policy"],
            )
