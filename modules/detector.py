def detect_hash(hash_string):
    """
    Detect the hash algorithm based on hash length.
    """

    hash_string = hash_string.strip().lower()

    length = len(hash_string)

    if length == 32:
        return "md5"

    elif length == 40:
        return "sha1"

    elif length == 56:
        return "sha224"

    elif length == 64:
        return "sha256"

    elif length == 96:
        return "sha384"

    elif length == 128:
        return "sha512"

    return None