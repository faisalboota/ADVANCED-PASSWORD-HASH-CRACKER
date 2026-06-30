import time
from tqdm import tqdm

from modules.hash_utils import generate_hash


def dictionary_attack(target_hash, algorithm, wordlist_path, verbose=False):

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
            passwords = file.readlines()

    except FileNotFoundError:
        return None

    attempts = 0
    start = time.time()

    iterator = tqdm(passwords, desc="Cracking", unit="password") if verbose else passwords

    for password in iterator:

        password = password.strip()

        if not password:
            continue

        attempts += 1

        if generate_hash(password, algorithm) == target_hash.lower():

            elapsed = time.time() - start

            return {
                "found": True,
                "password": password,
                "attempts": attempts,
                "time": elapsed,
                "speed": attempts / elapsed if elapsed > 0 else 0
            }

    elapsed = time.time() - start

    return {
        "found": False,
        "password": None,
        "attempts": attempts,
        "time": elapsed,
        "speed": attempts / elapsed if elapsed > 0 else 0
    }