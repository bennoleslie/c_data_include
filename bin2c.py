#!/usr/bin/env python3

import argparse
import os

def convert_file_to_c(infile, outfile=None, varname=None):
    if outfile is None:
        outfile = os.path.splitext(infile)[0] + '.c'
    if varname is None:
        varname = os.path.splitext(infile)[0]
    with open(infile, 'rb') as inf, open(outfile, 'wb') as outf:
        outf.write("char {}[] = {{\n".format(varname).encode())
        while True:
            ch = inf.read(1)
            if len(ch) == 0:
                break
            outf.write("    {}, \n".format(ord(ch)).encode())
        outf.write(b"};")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', metavar='FILE', nargs='+', help='an integer for the accumulator')

    args = parser.parse_args()
    for fn in args.files:
        convert_file_to_c(fn)


if __name__ == "__main__":
    main()
