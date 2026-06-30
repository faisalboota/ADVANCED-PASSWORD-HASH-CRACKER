from colorama import Fore, Style, init

init(autoreset=True)


def show_banner():
    print(Fore.CYAN + "=" * 65)
    print(Fore.GREEN + "      ADVANCED PASSWORD HASH CRACKER")
    print(Fore.YELLOW + "           Educational Edition v2.0")
    print(Fore.WHITE + "        Developed in Python for Learning")
    print(Fore.CYAN + "=" * 65)
    print(Style.RESET_ALL)