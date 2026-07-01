import time

from modules.hash_utils import generate_hash


def dictionary_attack(target_hash, algorithm, wordlist_path, verbose=False):
    """
    Perform a dictionary attack by reading the wordlist
    line by line. This is memory-efficient and works
    well with large files such as rockyou.txt.
    """

    attempts = 0
    start_time = time.time()

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:

            for line in file:

                password = line.strip()

                if not password:
                    continue

                attempts += 1

                if verbose and attempts % 1000 == 0:
                    elapsed = time.time() - start_time
                    speed = attempts / elapsed if elapsed > 0 else 0

                    print(
                        f"\rTested: {attempts:,} | "
                        f"Speed: {speed:,.0f} H/s | "
                        f"Current: {password[:25]}",
                        end=""
                    )

                if generate_hash(password, algorithm) == target_hash.lower():

                    elapsed = time.time() - start_time

                    if verbose:
                        print()

                    return {
                        "found": True,
                        "password": password,
                        "attempts": attempts,
                        "time": elapsed,
                        "speed": attempts / elapsed if elapsed > 0 else 0
                    }

        elapsed = time.time() - start_time

        if verbose:
            print()

        return {
            "found": False,
            "password": None,
            "attempts": attempts,
            "time": elapsed,
            "speed": attempts / elapsed if elapsed > 0 else 0
        }

    except FileNotFoundError:
        return None