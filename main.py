import os
import argparse

from git import Repo

repo = Repo(os.getcwd())

class GPushM:
    def __init__(self):
        pass
    
    def add_tag(tag):
        more[tag] = {}
    
    def add_tag_remote(tag, remote):
        if tag not in more:
            print("Tag Not Added!")

def gaddc(message):
    print(os.path.dirname(__file__))
    git = repo.git
    git.add(".")
    git.commit("-m", message)

def parser_gp():
    parser = argparse.ArgumentParser(description="combination and simplification of some useful git commands")
    subparser = parser.add_subparsers(help="commands")

    addc = subparser.add_parser("addc", help="add and commit")
    addc.add_argument("-m", "--message", help="commit message", required=True)

    args = parser.parse_args()
    if "message" in args:
        gaddc(args.message)
    
if __name__ == "__main__":
    parser_gp()