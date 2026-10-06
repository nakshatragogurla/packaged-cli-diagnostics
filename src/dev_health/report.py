import json

from .diagnostics import run_diagnostics


def determine_status(report):
    for tool in report["tools"].values():
        if not tool["installed"]:
            return "warn"

    return "pass"


def create_report():
    report = run_diagnostics()
    report["overall_status"] = determine_status(report)
    return report


def json_report(report):
    return json.dumps(report, indent=2)


def text_report(report):
    lines = []

    lines.append("Developer Environment Health Report")
    lines.append("=" * 40)

    lines.append("")
    lines.append("Python:")
    lines.append(f"  Version: {report['python']['version']}")
    lines.append(f"  Status: {report['python']['status'].upper()}")

    lines.append("")
    lines.append("Disk:")
    lines.append(f"  Free Space: {report['disk']['free_gb']} GB")
    lines.append(f"  Status: {report['disk']['status'].upper()}")

    lines.append("")
    lines.append("Developer Tools:")

    for name, info in report["tools"].items():
        if info["installed"]:
            lines.append(
                f"  {name}: {info['version']} PASS"
            )
        else:
            lines.append(
                f"  {name}: NOT FOUND WARN"
            )

    lines.append("")
    lines.append("Environment:")

    for name, value in report["environment"].items():
        lines.append(f"  {name}: {value.upper()}")

    lines.append("")
    lines.append(
        f"Overall Status: {report['overall_status'].upper()}"
    )

    return "\n".join(lines)