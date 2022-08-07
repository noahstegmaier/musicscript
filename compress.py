#!/usr/bin/env python
from argparse import ArgumentParser
from  tempfile import TemporaryDirectory
import os

def compress(indir,outdir):
    if not os.path.isdir(indir):
        print("input directory doesnt exist")
        exit(1)
    os.makedirs(outdir)
    with TemporaryDirectory() as ninjadir:
        print('created temporary directory', ninjadir)

def main():
    parser = ArgumentParser()
    parser.add_argument('-i','--input', required=True)
    parser.add_argument('-o','--output', required=True)
    args = parser.parse_args()
    compress(args.input, args.output)
    

if __name__ == "__main__":
    main()


