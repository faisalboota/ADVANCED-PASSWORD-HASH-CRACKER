import argparse

from modules.banner import show_banner


def create_parser():
    parser = argparse.ArgumentParser(
        prog="cracker.py",
        description="Educational Password Hash Cracker",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-H",
        "--hash",
        help="Target hash"
    )

    group.add_argument(
        "--generate",
        help="Generate hash from password"
    )

    group.add_argument(
        "--benchmark",
        action="store_true",
        help="Run benchmark"
    )

    parser.add_argument(
        "-m",
        "--method",
        choices=[
            "md5",
            "sha1",
            "sha224",
            "sha256",
            "sha384",
            "sha512"
        ],
        default="md5",
        help="Hash algorithm"
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        help="Wordlist file"
    )

    parser.add_argument(
        "--brute",
        action="store_true",
        help="Use brute-force attack"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose mode"
    )

    return parser


def main():
    show_banner()

    parser = create_parser()
    args = parser.parse_args()

    print("Arguments received:\n")

    for key, value in vars(args).items():
        print(f"{key:12}: {value}")


if __name__ == "__main__":
    main()