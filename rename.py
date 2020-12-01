
import argparse
import os

parser = argparse.ArgumentParser(description='Batch rename files...')
parser.add_argument("--p",help="Path to files",required=True,metavar="[/path/..]")
parser.add_argument("--n",help="Enter Name of file",required=True,metavar="[NAME]")
parser.add_argument("--e",help="Extension",default="",metavar=".txt")
args = parser.parse_args()



for count,filename in enumerate(os.listdir(args.p)):
    dest = str(args.n)+str(count)+str(args.e)
    src =args.p + filename
    dest =args.p + dest
    os.rename(src,dest)