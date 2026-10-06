from dev_health.diagnostics import (
    run_diagnostics,
    get_tool_version,
    validate_config_path,
)


def test_run_diagnostics():
    report = run_diagnostics()

    assert "python" in report
    assert "disk" in report
    assert "environment" in report
    assert "tools" in report

    assert "git" in report["tools"]
    assert "node" in report["tools"]
    assert "npm" in report["tools"]
    assert "java" in report["tools"]


def test_missing_dependency():
    result = get_tool_version("tool-that-does-not-exist")

    assert result["installed"] is False
    assert result["version"] is None


def test_malformed_config_path():
    assert validate_config_path("") is False
    assert validate_config_path("not-an-absolute-path") is False