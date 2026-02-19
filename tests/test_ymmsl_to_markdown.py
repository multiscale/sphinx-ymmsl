"""Tests for ymmsl_to_markdown module."""

from pathlib import Path

from sphinx_ymmsl.ymmsl_to_markdown import (
    components_markdown,
    conduits_markdown,
    extract_version_from_file,
    generate_document_header,
    generate_file_info,
    generate_header,
    generate_model_header,
    generate_supported_settings_markdown,
    model_markdown,
    ports_markdown,
    ymmsl_to_markdown,
)


class TestGenerateDocumentHeader:
    """Tests for generate_document_header function."""

    def test_document_header(self):
        """Test document header generation."""
        path = Path("/tmp/test_model.ymmsl")
        result = generate_document_header(path, "Test description")

        assert "# yMMSL Test Model Documentation" in result
        assert "Test description" in result


class TestGenerateHeader:
    """Tests for generate_header function."""

    def test_header_without_description(self):
        """Test header without description."""
        result = generate_header("Test Title", header_level=2)

        assert "## Test Title" in result
        assert len(result) == 1

    def test_header_with_description(self):
        """Test header with description."""
        result = generate_header("Test Title", "A description", header_level=2)

        assert "## Test Title" in result
        assert "A description" in result


class TestGenerateFileInfo:
    """Tests for generate_file_info function."""

    def test_file_info_with_version(self, temp_ymmsl_file, minimal_ymmsl):
        """Test file info generation with version."""
        temp_path = temp_ymmsl_file(minimal_ymmsl)
        result = generate_file_info(temp_path)

        assert f"**Model file**: `{temp_path.name}`" in result
        assert "**yMMSL version**: `v0.2`" in result


class TestExtractVersionFromFile:
    """Tests for extract_version_from_file function."""

    def test_extract_version(self, temp_ymmsl_file, minimal_ymmsl):
        """Test extracting version from file."""
        temp_path = temp_ymmsl_file(minimal_ymmsl)
        version = extract_version_from_file(temp_path)
        assert version == "v0.2"

    def test_extract_version_not_found(self, temp_ymmsl_file):
        """Test when version is not found in file."""
        temp_path = temp_ymmsl_file("description: Test\n")
        version = extract_version_from_file(temp_path)
        assert version is None


class TestModelMarkdown:
    """Tests for model_markdown function."""

    def test_no_models(self, load_ymmsl_config, minimal_ymmsl):
        """Test with yMMSL file containing no models section."""
        cfg = load_ymmsl_config(minimal_ymmsl)
        result = model_markdown(cfg)
        assert result == ""

    def test_single_model(self, load_ymmsl_config, ymmsl_with_model):
        """Test with yMMSL file containing a minimal model."""
        cfg = load_ymmsl_config(ymmsl_with_model)
        result = model_markdown(cfg)
        assert "## Models" in result
        assert "### Test Model" in result


class TestGenerateModelHeader:
    """Tests for generate_model_header function."""

    def test_model_header(self):
        """Test model header generation."""
        result = generate_model_header("test_model", "A test model")
        assert "### Test Model" in result
        assert "A test model" in result


class TestGenerateSupportedSettingsMarkdown:
    """Tests for generate_supported_settings_markdown function."""

    def test_empty_settings(self, load_ymmsl_config, ymmsl_with_model):
        """Test with yMMSL model that has no supported settings."""
        cfg = load_ymmsl_config(ymmsl_with_model)
        model = cfg.models["test_model"]
        result = generate_supported_settings_markdown(model.supported_settings)
        assert result == []

    def test_single_setting(self, load_ymmsl_config, ymmsl_with_settings):
        """Test with yMMSL model containing a single supported setting."""
        cfg = load_ymmsl_config(ymmsl_with_settings)
        model = cfg.models["test_model"]
        result = generate_supported_settings_markdown(model.supported_settings)
        result_str = "\n".join(result)

        assert "#### Supported Settings" in result
        assert "| Parameter | Type | Description |" in result_str
        assert "| timestep | float | Timestep value |" in result_str


class TestConduitsMarkdown:
    """Tests for conduits_markdown function."""

    def test_empty_conduits(self, load_ymmsl_config, ymmsl_with_model):
        """Test with yMMSL model that has no conduits."""
        cfg = load_ymmsl_config(ymmsl_with_model)
        model = cfg.models["test_model"]
        result = conduits_markdown(model.conduits)
        assert result == []

    def test_single_conduit(self, load_ymmsl_config, ymmsl_with_conduits):
        """Test with yMMSL model containing a single conduit."""
        cfg = load_ymmsl_config(ymmsl_with_conduits)
        model = cfg.models["test_model"]
        result = conduits_markdown(model.conduits)

        assert "#### Conduits" in result
        assert "* test.state_out: test.init_in" in result


class TestComponentsMarkdown:
    """Tests for components_markdown function."""

    def test_empty_components(self, load_ymmsl_config, ymmsl_with_model):
        """Test with yMMSL model that has no components."""
        cfg = load_ymmsl_config(ymmsl_with_model)
        model = cfg.models["test_model"]
        result = components_markdown(model.components)
        assert result == []

    def test_single_component(self, load_ymmsl_config, ymmsl_with_min_component):
        """Test with yMMSL model containing a single component."""
        cfg = load_ymmsl_config(ymmsl_with_min_component)
        model = cfg.models["test_model"]
        result = components_markdown(model.components)

        assert "#### Comp" in result
        assert "This is a component" in result


class TestPortsMarkdown:
    """Tests for ports_markdown function."""

    def test_empty_ports(self, load_ymmsl_config, ymmsl_with_min_component):
        """Test with yMMSL component that has no ports."""
        cfg = load_ymmsl_config(ymmsl_with_min_component)
        component = cfg.models["test_model"].components["comp"]
        result = ports_markdown(component.ports)
        assert result == []

    def test_single_port(self, load_ymmsl_config, ymmsl_with_port):
        """Test with yMMSL component containing a single port."""
        cfg = load_ymmsl_config(ymmsl_with_port)
        component = cfg.models["test_model"].components["comp"]
        result = ports_markdown(component.ports)
        result_str = "\n".join(result)

        assert "| Operator | Port Name |" in result_str
        assert "| O_I | state_out |" in result_str

    def test_with_header(self, load_ymmsl_config, ymmsl_with_port):
        """Test with custom header."""
        cfg = load_ymmsl_config(ymmsl_with_port)
        component = cfg.models["test_model"].components["comp"]
        result = ports_markdown(
            component.ports, header_level=3, header_text="Model Ports"
        )

        assert "### Model Ports" in result


class TestYmmslToMarkdown:
    """Integration test for ymmsl_to_markdown function."""

    def test_complete_ymmsl_file(self, temp_ymmsl_file, ymmsl_with_model):
        """Test with a complete yMMSL file."""
        temp_path = temp_ymmsl_file(ymmsl_with_model)
        result = ymmsl_to_markdown(temp_path)

        assert "# yMMSL" in result
        assert "Documentation" in result
        assert "**Model file**:" in result
        assert "**yMMSL version**: `v0.2`" in result
        assert "A test model" in result

    def test_ymmsl_file_without_models(self, temp_ymmsl_file, minimal_ymmsl):
        """Test with a yMMSL file that has no models section."""
        temp_path = temp_ymmsl_file(minimal_ymmsl)
        result = ymmsl_to_markdown(temp_path)

        assert "# yMMSL" in result
        assert "Documentation" in result
        assert "Minimal test configuration" in result
        # Should not have Models section
        assert "## Models" not in result
