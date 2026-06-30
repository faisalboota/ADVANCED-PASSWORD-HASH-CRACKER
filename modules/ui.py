from colorama import Fore, Style, init

init(autoreset=True)


def info(message):
    print(Fore.CYAN + "[*] " + message)


def success(message):
    print(Fore.GREEN + "[+] " + message)


def warning(message):
    print(Fore.YELLOW + "[!] " + message)


def error(message):
    print(Fore.RED + "[-] " + message)


def title(message):
    print(Fore.BLUE + "=" * 60)
    print(Fore.WHITE + message.center(60))
    print(Fore.BLUE + "=" * 60)