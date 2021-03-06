import os
from sys import exit
import json
import argparse

from git import Repo
  
cdir = os.getcwd() + "/.git"

def init(dir):
    if dir == ".":
        gpdir = cdir
    else:
        gpdir = os.path.join(dir, ".git")
    with open(gpdir+"/config.json", "w") as f:
        f.write("{}")
        
class GPushC:
    def __init__(self, git):
        with open(cdir+"/config.json", "r") as f:
            content = json.load(f)
        self.c = content
        self.git = git
                
    def update_json(self, data):
        with open(cdir+"/config.json", "r+") as f:
            json.dump(data, f)
    
    def add_tag(self, tag):
        self.c[tag] = {}
        self.update_json(self.c)
        
    def add_tag_remote(self, tag, name, remote):
        if tag not in self.c:
            print("Tag Not Added!")
            return
        self.c[tag][name] = remote
        self.update_json(self.c)
        
    def push_tag(self, tag):
         for tag in self.c[tag].values():
             self.git.push(tag)

class Simplify:
    def __init__(self, git):
        self.git = git
    
    def gaddc(self, message):
        self.git.add(".")
        self.git.commit("-m", message)

def parser_gp():
    parser = argparse.ArgumentParser(description="combination and simplification of some useful git commands")
        
    subparser = parser.add_subparsers(help="main commands")
    
    gpinit = subparser.add_parser("init", help="make it a gp directory")
    gpinit.add_argument("-d", "--dir", help="init which dir", default=".", dest="dir")
    
    pushc = subparser.add_parser("pushc", help="push as tags")
    pushc_sub = pushc.add_subparsers(help="pushc", dest="pushc")
    pushc_addt = pushc_sub.add_parser("addt", help="add tag of remote repos")
    pushc_addt.add_argument("-t", "--tag", help="tag name", required=True)
    pushc_addr = pushc_sub.add_parser("addr", help="add remote git repo to tag")
    pushc_addr.add_argument("-t", "--tag", help="where the remote to be added", required=True)
    pushc_addr.add_argument("-n", "--name", help="the name for the remote", required=True)
    pushc_addr.add_argument("-r", "--remote", help="the git repo url", required=True)
    pushc_pusht = pushc_sub.add_parser("pusht", help="push the change to each of tag")
    pushc_pusht.add_argument("-t", "--tag", help="push as a tag", required=True)

    addc = subparser.add_parser("addc", help="add and commit")
    addc.add_argument("-m", "--message", help="commit message", required=True)

    args = parser.parse_args()
    print(args)
    
    if "dir" in args:
        init(args.dir)
        exit()
    
    try:
        repo = Repo(".")
    except Exception as e:
        print("Invalid or Not a Git Repo")
        exit()
   
    git = repo.git
    gpushc = GPushC(git)
    simplify = Simplify(git)
    
    if "message" in args:
        simplify.gaddc(args.message)
    elif "pushc" in args:
        if args.pushc == "addt":
            gpushc.add_tag(args.tag)
        elif args.pushc == "addr":
            gpushc.add_tag_remote(args.tag, args.name, args.remote)
        elif args.pushc == "pusht":
            gpushc.push_tag(args.tag)
    
if __name__ == "__main__":
    parser_gp()