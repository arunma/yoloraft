def test_config_with_custom_values(config):
    assert config.cluster_name == "yolo"
    assert config.id == "a"
    assert config.data_dir == "a/data"
    assert config.listen_raft == "0.0.0.0:5091"
    assert config.peers["b"] == "0.0.0.0:5092"
    assert config.peers["c"] == "0.0.0.0:5093"
    assert config.election_timeout_min == 150
    assert config.election_timeout_max == 300
    assert config.heartbeat_interval == 50
    assert config.max_payload_entries == 100
    assert config.replication_lag_threshold == 100
    assert config.snapshot_policy["logs_since_last_snapshot"] == 10
    assert config.snapshot_policy["snapshot_max_chunk_size"] == 3000000
