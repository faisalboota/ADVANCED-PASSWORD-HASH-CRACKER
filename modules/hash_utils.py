import hashlib


SUPPORTED_HASHES = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
}


def generate_hash(password: str, algorithm: str) -> str:
    """
    Generate a hash from a password.
    """

    algorithm = algorithm.lower()

    if algorithm not in SUPPORTED_HASHES:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")

    hasher = SUPPORTED_HASHES[algorithm]()
    hasher.update(password.encode("utf-8"))

    return hasher.hexdigest()


def verify_hash(password: str, target_hash: str, algorithm: str) -> bool:
    """
    Verify whether a password matches a given hash.
    """

    return generate_hash(password, algorithm) == target_hash.lower()


def list_algorithms():
    """
    Return supported algorithms.
    """

    return list(SUPPORTED_HASHES.keys())