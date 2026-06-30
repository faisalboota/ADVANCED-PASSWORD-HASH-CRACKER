import argparse

from modules.banner import show_banner
from modules.hash_utils import generate_hash


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
        help="Generate hash from a password"
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
    # Show banner
    show_banner()

    # Parse command-line arguments
    parser = create_parser()
    args = parser.parse_args()

    # Generate hash
    if args.generate:
        password_hash = generate_hash(args.generate, args.method)

        print(f"Algorithm : {args.method.upper()}")
        print(f"Password  : {args.generate}")
        print(f"Hash      : {password_hash}")
        return

    # Benchmark (placeholder)
    if args.benchmark:
        print("Benchmark module will be added in a later part.")
        return

    # Crack hash (placeholder)
    if args.hash:
        print("Hash Cracking Module")
        print("-" * 40)
        print(f"Target Hash : {args.hash}")
        print(f"Algorithm   : {args.method.upper()}")

        if args.wordlist:
            print(f"Wordlist    : {args.wordlist}")

        if args.brute:
            print("Attack Mode : Brute Force")

        print("\n(Dictionary attack engine will be added in Part 3.)")
        return


if __name__ == "__main__":
    main()