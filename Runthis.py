from colorama import Fore, init
from lib import member_dict, Debater, print_member, read, Room
from matching import match, allocate
from os import system
init(autoreset=True)

success = lambda input: f"{Fore.GREEN}{input}"
failure = lambda input: f"{Fore.RED}{input}"



def repl() -> None:
    participants = {}
    while True:
        _in = input(success("Chronos $$$ "))
        
        if _in == "read":
            print(success(_in))
            read(participants)
        
        elif _in == "ls -m":
            print(success(_in))
            print_member(member_dict)

        elif _in == "ls -p":
            print(success(_in))
            print_member(participants)

        elif _in == "ls -lp":
            print(success(_in))
            print_member(participants,1)

        elif _in == "cls-w":
            print(success(_in))
            system("cls")

        elif _in == "cls-l":
            print(success(_in))
            system("clear")

        elif _in == "\n":
            print(success(_in))
            pass

        elif _in == "-e":
            print("Exit")
            break
        
        elif _in == "-h":
            print()
            print("|  read    | read from .txt file")
            print("|  -m      | Test the number of auto allocated rooms")
            print("|  -a      | Allocate members to Rooms")
            print("|  ls -m   | list all member in database")
            print("|  ls -p   | list all participants today in short")
            print("|  ls -lp  | list all participants today in detail")
            print("|  cls-w   | clear console for windows")
            print("|  cls-l   | clear console for linux/Mac")
            print("|  -e      | Exit")

        elif _in == "-m":
            if len(participants) == 0:
                print(failure("Participant empty, plz read the txt first"))
            else:
                match(participants)

        elif _in == "-a":
            if len(participants) == 0:
                print(failure("Participant empty, plz read the txt first"))
            else:
                allocate(participants)

        else:
            print(failure("Unknown command, "))


if __name__ == "__main__":
    print()
    print(success("Welcome to chronos-REPL, For standard room allocation:"))
    print(success("     1. type read to read the txt file"))
    print(success("     2. (NOT NECESSARY) type -m   to check if the match is proper "))
    print(success("     3. type -a   to allocate members, -a provides different result each time"))
    print("\n")
    print(success("type -h for more info, type -e to quit"))
    print()
    repl()