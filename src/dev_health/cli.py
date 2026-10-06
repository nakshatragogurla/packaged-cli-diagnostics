import argparse

from .report import create_report, json_report, text_report


def main():
    parser = argparse.ArgumentParser(
        description="Developer environment diagnostics tool"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output the report as JSON"
    )

    args = parser.parse_args()

    report = create_report()

    if args.json:
        print(json_report(report))
    else:
        print(text_report(report))

    if report["overall_status"] == "pass":
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())