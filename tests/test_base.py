def test_base(config):
    assert config["id"] == "a"
    assert config["data_dir"] == "a/data"
    assert config["listen_raft"] == "0.0.0.0:5091"
    assert len(config["peers"]) == 2
    assert config["peers"]["b"] == "0.0.0.0:5092"
    assert config["peers"]["c"] == "0.0.0.0:5093"
