import os
import argparse

from git import Repo

repo = Repo(".")

def gaddc(message):
    git = repo.git
    git.add(".")
    git.commit("-m", message)

def parser_gp():
    parser = argparse.ArgumentParser(description="combination and simplification of some useful git commands")
    subparser = parser.add_subparsers(help="commands")

    addc = subparser.add_parser("addc", help="add and commit")
    addc.add_argument("-m", "--message", help="commit message", required=True)

    args = parser.parse_args()
    print(args)
    if "message" in args:
        gaddc(args.message)
    
if __name__ == "__main__":
    parser_gp()