"""Handler for WPK-2103: Audit Trail Compactor."""
import argparse


def self_check() -> bool:
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        raise SystemExit(0 if self_check() else 1)


if __name__ == "__main__":
    main()
