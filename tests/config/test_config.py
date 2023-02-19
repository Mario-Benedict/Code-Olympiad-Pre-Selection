from mariar.config.config import config

def test_config():
  assert config is not None and len(list(config.keys())) > 0
