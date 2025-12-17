import argparse
import json
from core import analyze_url


def main():
    parser = argparse.ArgumentParser(
        description="Detect authentication components in a website's HTML."
    )
    parser.add_argument(
        "url",
        help="Website URL to analyze (e.g., https://github.com/login)"
    )

    args = parser.parse_args()

    try:
        result = analyze_url(args.url)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=2))


if __name__ == "__main__":
    main()
