#!python3

import re
import json
import argparse
import unicodedata
import itertools
from typing import Iterator, Tuple

from pypinyin import lazy_pinyin


def main():
    argument_parser = argparse.ArgumentParser('convert.py', usage='convert.py [JSON_FILE]')
    argument_parser.add_argument('file', type=argparse.FileType('r'))
    args = argument_parser.parse_args()
    idioms = json.load(args.file)
    results = dict()
    for entry in idioms:
        for word in re.split('，|、', entry['word']):
            pinyin = "'".join(lazy_pinyin(word))
            results.setdefault(word, pinyin)

    for word, pinyin in sorted(results.items()):
        print(f'{word}\t{pinyin}\t0')


if __name__ == '__main__':
    main()
