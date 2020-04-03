"""start using diff tool"""
import os
from argparse import ArgumentParser
from src import diff


if __name__ == '__main__':
    parser = ArgumentParser(description='Add missing translations in destination-file.')
    parser.add_argument(
        '--diff',
        default=False,
        action='store_true',
        help='Find different keyvalues and select the correct one manually.')
    parser.add_argument(
        '--auto',
        default=False,
        action='store_true',
        help='In automode additional keys will automatically be added.')
    parser.add_argument(
        'src_file', metavar='src_file', type=str,
        help='Specify a source file where all translations exists.')
    parser.add_argument(
        'dst_file', metavar='dst_file', type=str,
        help='Specify a destination file where translations are missing.')
    parser.add_argument(
        '--out', type=str,
        default='./data/out/outfile.json',
        help='Specify the destination the new file should be written.')
    ARGS = parser.parse_args()
    DIRNAME = os.path.dirname(__file__)
    DIFF = diff.Diff(ARGS.src_file, ARGS.dst_file, ARGS.out)
    DIFF.display_count_keys_not_in_dst()
    if ARGS.diff:
        DIFF.compare_keys()
    else:
        DIFF.add_missing_keys(ARGS.auto)
        DIFF.write_file(os.path.join(DIRNAME))

