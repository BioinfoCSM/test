#/usr/bin/python
# coding=utf-8

import argparse

parser = argparse.ArgumentParser (description = "help document", help = "aa")
parser.add_argument ("-n", "--name", type = str, help = "your name", 
        required = False, default = "csm", choices = ["csm", "bgi"])
args = parser.parse_args ()

print (args.name, args.age)

