#!/usr/bin/env python
from argparse import ArgumentParser
import shutil
from tempfile import TemporaryDirectory
import os
from pathlib import Path


def escape_ninja_path(file_path):
    char_to_replace = {' ': '$ ',
                       '$': '$$',
                       ':': '$:'}
    return file_path.translate(str.maketrans(char_to_replace))


def compress(indir, outdir):
    if shutil.which('opusenc') is None:
        print("please install opus-tools")
        exit(1)
    if not os.path.isdir(indir):
        print("input directory doesnt exist")
        exit(1)
    os.makedirs(outdir, exist_ok=True)
    with TemporaryDirectory() as ninjadir:
        #print('created temporary directory', ninjadir)

        with open("compress.ninja", 'w') as nfile:
            nfile.write("flags = --bitrate 128 --discard-pictures\n")
            nfile.write("rule opus\n")
            nfile.write(" command = opusenc $flags $in $out\n")

            fileendings = [".wav", ".flac"]
            for (path, _, files) in os.walk(indir):
                for file in files:
                    rel_path = Path(path).relative_to(indir)
                    if Path(file).suffix in fileendings:
                        inpath = os.path.join(path, file)
                        new_path = rel_path.joinpath(
                            Path(file).with_suffix(".opus"))
                        outpath = Path(outdir).absolute().joinpath(new_path)
                        escaped_outpath = escape_ninja_path(str(outpath))
                        escaped_inpath = escape_ninja_path(inpath)
                        nfile.write(f"build {escaped_outpath}: opus {escaped_inpath}\n")


def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', required=True)
    args = parser.parse_args()
    compress(args.input, args.output)


if __name__ == "__main__":
    main()
