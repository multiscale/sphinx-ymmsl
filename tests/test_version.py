import importlib.metadata


def test_version():
    version = importlib.metadata.version("sphinx_ymmsl")
    assert "unknown" not in version
    assert version != ""
