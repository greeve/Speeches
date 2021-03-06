#!/usr/bin/env python3

"""
Download Conference Addresses for the apostles from churchofjesuschrist.org

python core.py YYYY MM
"""

__author__ = "Greg Reeve"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import extractor
import ebook

from logger import setup_logger

logger = setup_logger(logfile=None)


def main(args):
    """
    Main entry point of the app
    """
    logger.info(args)
    talks = []
    for lang in args.languages:
        slugs = extractor.get_slugs(args.year, args.month, lang)
        paths = extractor.write_talks(slugs, args.year, args.month, lang)
        talks.extend(paths)
    ebook.generate_files(args.year, args.month, args.languages, talks)
    ebook.create(args.year, args.month)


if __name__ == "__main__":
    """
    This is executed when run from the command line
    """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("year", help="The year of the conference (e.g. 2017).")
    parser.add_argument(
        "month",
        help="The month of the conference (i.e. 04 or 10).",
    )

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument(
        '-l',
        '--languages',
        action='store',
        dest='languages',
        default=['eng', 'hun'],
        nargs='+',
    )

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)",
    )

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__),
    )

    args = parser.parse_args()
    main(args)
