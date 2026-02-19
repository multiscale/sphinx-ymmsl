"""Shared pytest fixtures for sphinx-ymmsl tests."""

import tempfile
from pathlib import Path
from typing import Generator

import pytest
import ymmsl


@pytest.fixture
def minimal_ymmsl() -> str:
    """Minimal valid yMMSL content."""
    return """ymmsl_version: v0.2

description: Minimal test configuration
"""


@pytest.fixture
def ymmsl_with_model() -> str:
    """yMMSL content with a minimal model."""
    return """ymmsl_version: v0.2

description: Configuration with model

models:
  test_model:
    description: A test model
"""


@pytest.fixture
def ymmsl_with_settings() -> str:
    """yMMSL content with supported settings."""
    return """ymmsl_version: v0.2

description: Configuration with supported settings

models:
  test_model:
    description: A test model
    supported_settings:
      timestep: float  Timestep value
"""


@pytest.fixture
def ymmsl_with_conduits() -> str:
    """yMMSL content with conduits."""
    return """ymmsl_version: v0.2

description: Configuration with conduits

models:
  test_model:
    description: A test model
    conduits:
      test.state_out: test.init_in
"""


@pytest.fixture
def ymmsl_with_min_component() -> str:
    """yMMSL content with a single component."""
    return """ymmsl_version: v0.2

description: Configuration with component

models:
  test_model:
    description: Model with components
    components:
      comp:
        ports: {}
        description: This is a component
"""


@pytest.fixture
def ymmsl_with_full_component() -> str:
    """yMMSL content with component that has description."""
    return """ymmsl_version: v0.2

description: Configuration with fully described component

models:
  test_model:
    description: Model with fully described components
    components:
      comp:
        ports:
          o_i: out
        description: This is a component
        implementation: comp_program
        multiplicity: 1
"""


@pytest.fixture
def ymmsl_with_port() -> str:
    """yMMSL content with a component containing a port."""
    return """ymmsl_version: v0.2

description: Configuration with port

models:
  test_model:
    description: Model with ports
    components:
      comp:
        ports:
          o_i: state_out
        description: Component with port
"""


@pytest.fixture
def temp_ymmsl_file() -> Generator[callable, None, None]:
    """
    Create a temporary yMMSL file.
    """
    created_files = []

    def _create_file(content: str) -> Path:
        f = tempfile.NamedTemporaryFile(mode="w", suffix=".ymmsl", delete=False)
        f.write(content)
        f.close()
        path = Path(f.name)
        created_files.append(path)
        return path

    yield _create_file

    for path in created_files:
        if path.exists():
            path.unlink()


@pytest.fixture
def load_ymmsl_config(temp_ymmsl_file) -> callable:
    """
    Load the yMMSL file at a given path and return the configuration.
    """

    def _load_config(content: str) -> ymmsl.v0_2.Configuration:
        path = temp_ymmsl_file(content)
        return ymmsl.load_as(ymmsl.v0_2.Configuration, path)

    return _load_config
