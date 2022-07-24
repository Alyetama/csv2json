#!/usr/bin/env python
# coding: utf-8

import argparse
import json
import time
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd


def opts() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path',
        nargs='+',
        help='Path to a single file/directory or multiple files/directories')
    parser.add_argument(
        '-o',
        '--orient',
        help='The type of the values of the dictionary',
        choices=['dict', 'list', 'series', 'split', 'records', 'index'],
        default='records')
    parser.add_argument('-i',
                        '--indent',
                        help='JSON output indentation',
                        default=4)
    parser.add_argument('-c',
                        '--compress',
                        help='Compress the output',
                        action='store_true')
    return parser.parse_args()


def main():
    args = opts()
    output_dir = Path(f'csv2json_output_{int(time.time())}')
    output_dir.mkdir()
    paths = [Path(x) for x in args.path]

    for path in paths:
        if path.is_dir():
            paths.remove(path)
            paths += list(path.glob('**/*.csv'))

    for path in paths:
        out_file = Path(f'{output_dir}/{path.stem}.json')
        with open(out_file, 'w') as j:
            data = pd.read_csv(path).replace({
                np.nan: None
            }).to_dict(args.orient)
            json.dump(data, j, indent=args.indent)

        if args.compress:
            with zipfile.ZipFile(out_file.with_suffix('.zip'),
                                 mode='w',
                                 compression=zipfile.ZIP_DEFLATED,
                                 compresslevel=9) as zf:
                zf.write(out_file, out_file.name)
            out_file.unlink()

    print(f'\nOutput location:\n\t{output_dir.absolute()}')


if __name__ == '__main__':
    main()
