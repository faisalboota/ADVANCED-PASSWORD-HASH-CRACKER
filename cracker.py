import argparse

from modules.banner import show_banner
from modules.hash_utils import generate_hash
from modules.attacks import dictionary_attack
from modules.detector import detect_hash
from modules.reporter import save_text_report, save_json_report
from modules.session import save_session
from modules.benchmark import run_benchmark
from modules.ui import title, info, success, error


def create_parser():
    parser = argparse.ArgumentParser(
        prog="cracker.py",
        description="Advanced Password Hash Cracker (Educational Edition)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-H", "--hash", help="Target hash")
    group.add_argument("--generate", help="Generate hash from password")
    group.add_argument(
        "--benchmark",
        action="store_true",
        help="Run benchmark"
    )

    parser.add_argument(
        "-m",
        "--method",
        default="auto",
        choices=[
            "auto",
            "md5",
            "sha1",
            "sha224",
            "sha256",
            "sha384",
            "sha512"
        ],
        help="Hash algorithm"
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        help="Wordlist path"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output"
    )

    parser.add_argument(
        "--brute",
        action="store_true",
        help="Brute-force mode (Coming Soon)"
    )

    return parser


def generate_mode(args):

    algorithm = args.method

    if algorithm == "auto":
        algorithm = "md5"

    password_hash = generate_hash(
        args.generate,
        algorithm
    )

    title("HASH GENERATED")

    info(f"Algorithm : {algorithm.upper()}")
    info(f"Password  : {args.generate}")
    info(f"Hash      : {password_hash}")


def benchmark_mode():

    title("BENCHMARK")

    algorithms = [
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512"
    ]

    for algorithm in algorithms:

        result = run_benchmark(algorithm)

        print(
            f"{result['algorithm']:8}"
            f"{result['speed']:,.0f} Hashes/sec"
        )


def dictionary_mode(args):

    if not args.wordlist:
        error("Please specify a wordlist using -w")
        return

    algorithm = args.method

    if algorithm == "auto":

        algorithm = detect_hash(args.hash)

        if algorithm is None:
            error("Unable to detect hash type.")
            return

        title("HASH DETECTION")
        success(f"Detected : {algorithm.upper()}")

    title("DICTIONARY ATTACK")

    info(f"Target Hash : {args.hash}")
    info(f"Algorithm   : {algorithm.upper()}")
    info(f"Wordlist    : {args.wordlist}")

    result = dictionary_attack(
        target_hash=args.hash,
        algorithm=algorithm,
        wordlist_path=args.wordlist,
        verbose=args.verbose
    )

    if result is None:
        error("Wordlist not found.")
        return

    print()

    title("RESULT")

    if result["found"]:
        success("PASSWORD FOUND")
        print(f"Password : {result['password']}")
    else:
        error("PASSWORD NOT FOUND")

    print(f"Attempts : {result['attempts']:,}")
    print(f"Time     : {result['time']:.3f} sec")
    print(f"Speed    : {result['speed']:.0f} H/s")

    report = {
        "algorithm": algorithm.upper(),
        "hash": args.hash,
        "found": result["found"],
        "password": result["password"],
        "attempts": result["attempts"],
        "time": result["time"],
        "speed": result["speed"]
    }

    txt_file = save_text_report(report)
    json_file = save_json_report(report)
    save_session(report)

    print()

    success("Reports Saved")
    print(f"TXT Report   : {txt_file}")
    print(f"JSON Report  : {json_file}")
    print("Session Log  : sessions/history.log")


def main():

    show_banner()

    parser = create_parser()
    args = parser.parse_args()

    if args.generate:
        generate_mode(args)
        return

    if args.hash:
        dictionary_mode(args)
        return

    if args.benchmark:
        benchmark_mode()
        return


if __name__ == "__main__":
    main()