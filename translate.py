"""start using diff tool"""
import os
from argparse import ArgumentParser
from src import diff


if __name__ == '__main__':
    parser = ArgumentParser(description='Add missing translations in destination-file.')
    parser.add_argument(
        'src_file', metavar='src_file', type=str,
        help='Specify a source file where all translations exists.')
    parser.add_argument(
        'dst_file', metavar='dst_file', type=str,
        help='Specify a destination file where translations are missing.')
    ARGS = parser.parse_args()
    print(ARGS.src_file)
    print(ARGS.dst_file)
    DIRNAME = os.path.dirname(__file__)
    DIFF = diff.Diff(ARGS.src_file, ARGS.dst_file)
    DIFF.display_count_keys_not_in_dst()
    DIFF.add_missing_keys()
    DIFF.write_dst_file(os.path.join(DIRNAME, './data/en1.json'))
