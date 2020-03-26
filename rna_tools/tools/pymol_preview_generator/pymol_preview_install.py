#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import argparse
import os
from rna_tools import rna_tools_lib

def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="be verbose")
    parser.add_argument("shell", help="", default="")
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    if args.shell == 'bash':
        p = rna_tools_lib.get_rna_tools_path() + '/tools/pymol_preview_generator/bash/PyMOL Preview.workflow'
        cmd = "cp -rv '" + p + "' ~/Library/Services/"
        os.system(cmd)
    elif args.shell == 'zsh':        
        p = rna_tools_lib.get_rna_tools_path() + '/tools/pymol_preview_generator/zsh/PyMOL Preview.workflow'
        cmd = "cp -rv '" + p + "' ~/Library/Services/"
        os.system(cmd)
    else:
        print('select shell as bash or zsh')
