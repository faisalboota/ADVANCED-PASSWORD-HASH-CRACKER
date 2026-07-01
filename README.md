# Advanced Password Hash Cracker (Educational Edition)

A beginner-friendly Python cybersecurity project that demonstrates how password hashes work and how dictionary attacks can be performed in a safe, educational environment.

> **Educational Use Only:** This project is designed for learning, demonstrations, and authorized testing only.

---

## Features

* Generate password hashes
* Supported algorithms:

  * MD5
  * SHA1
  * SHA224
  * SHA256
  * SHA384
  * SHA512
* Dictionary attack using custom wordlists
* Automatic hash detection
* Progress display
* Benchmark mode
* TXT report generation
* JSON report generation
* Session history logging
* Large wordlist support
* Modular Python code
* Command-line interface

---

## Project Structure

```
Advanced-Password-Hash-Cracker/

├── cracker.py
├── README.md
├── LICENSE
├── requirements.txt
│
├── modules/
│   ├── attacks.py
│   ├── banner.py
│   ├── benchmark.py
│   ├── detector.py
│   ├── hash_utils.py
│   ├── progress.py
│   ├── reporter.py
│   ├── session.py
│   └── ui.py
│
├── wordlists/
├── reports/
├── sessions/
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Advanced-Password-Hash-Cracker.git
```

Open the project:

```bash
cd Advanced-Password-Hash-Cracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Generate an MD5 hash:

```bash
python cracker.py --generate password
```

Generate a SHA256 hash:

```bash
python cracker.py --generate password -m sha256
```

Dictionary attack:

```bash
python cracker.py -H HASH_VALUE -w wordlists/test_words.txt
```

Verbose mode:

```bash
python cracker.py -H HASH_VALUE -w wordlists/test_words.txt -v
```

Benchmark:

```bash
python cracker.py --benchmark
```

Help:

```bash
python cracker.py --help
```

---

## Sample Output

```
Password Found

Password : password

Attempts : 5
Time     : 0.003 sec
Speed    : 1500 H/s
```

---

## Technologies Used

* Python 3
* argparse
* hashlib
* colorama
* tqdm
* JSON
* Git
* GitHub

---

## Learning Objectives

This project helps demonstrate:

* Password hashing
* Secure password storage concepts
* Dictionary attacks
* Command-line application development
* File handling
* Report generation
* Performance benchmarking
* Modular programming
* Version control with Git

---

## Screenshots

Store project screenshots inside the **screenshots/** folder.

Suggested screenshots:

* Banner
* Generate Hash
* Dictionary Attack
* Benchmark
* Reports
* Session Log

---

## Disclaimer

This project is intended for educational purposes only.

Do not use this software against systems, accounts, or data without explicit authorization. The author is not responsible for misuse.

---

## Author

**Faisal Boota**

Cybersecurity Student

---

## License

This project is licensed under the MIT License.
