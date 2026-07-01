import time

from modules.hash_utils import generate_hash


def run_benchmark(algorithm, seconds=5):
    """
    Measure how many hashes can be generated per second.
    """

    start = time.time()
    count = 0

    while True:
        generate_hash(f"password{count}", algorithm)
        count += 1

        elapsed = time.time() - start

        if elapsed >= seconds:
            break

    return {
        "algorithm": algorithm.upper(),
        "hashes": count,
        "seconds": elapsed,
        "speed": count / elapsed
    }