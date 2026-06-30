import argparse

from modules.banner import show_banner
from modules.hash_utils import generate_hash
from modules.attacks import dictionary_attack
from modules.ui import title, info, success, error


def create_parser():
    parser = argparse.ArgumentParser(
        prog="cracker.py",
        description="Advanced Password Hash Cracker (Educational Edition)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-H",
        "--hash",
        help="Target hash to crack"
    )

    group.add_argument(
        "--generate",
        help="Generate hash from a password"
    )

    group.add_argument(
        "--benchmark",
        action="store_true",
        help="Run benchmark (Coming Soon)"
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
        help="Brute-force attack (Coming Soon)"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show progress while cracking"
    )

    return parser


def generate_mode(args):
    password_hash = generate_hash(args.generate, args.method)

    title("HASH GENERATED")

    info(f"Algorithm : {args.method.upper()}")
    info(f"Password  : {args.generate}")
    info(f"Hash      : {password_hash}")


def benchmark_mode():
    title("BENCHMARK")

    info("Benchmark module will be added in a future update.")


def dictionary_mode(args):

    if not args.wordlist:
        error("Please specify a wordlist using -w")
        return

    title("DICTIONARY ATTACK")

    info(f"Target Hash : {args.hash}")
    info(f"Algorithm   : {args.method.upper()}")
    info(f"Wordlist    : {args.wordlist}")

    result = dictionary_attack(
        target_hash=args.hash,
        algorithm=args.method,
        wordlist_path=args.wordlist,
        verbose=args.verbose
    )

    if result is None:
        error("Wordlist not found.")
        return

    print()

    title("RESULT")

    if result["found"]:
        success("Password Found")
        print(f"Password : {result['password']}")
    else:
        error("Password Not Found")

    print(f"Attempts : {result['attempts']:,}")
    print(f"Time     : {result['time']:.3f} seconds")
    print(f"Speed    : {result['speed']:.0f} H/s")


def main():

    show_banner()

    parser = create_parser()
    args = parser.parse_args()

    if args.generate:
        generate_mode(args)
        return

    if args.benchmark:
        benchmark_mode()
        return

    if args.hash:
        dictionary_mode(args)
        return


if __name__ == "__main__":
    main()