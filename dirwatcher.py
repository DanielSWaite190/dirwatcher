#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

import argparse
import logging
import signal
import time
import sys
import os

exit_flag = False

logging.basicConfig(
    format="%(asctime)s %(message)s"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    """Creates parsing arguments."""

    parser = argparse.ArgumentParser(
        description="Searches a given directory for a specific line of text")
    parser.add_argument(
        "directory", help="The directory that will be scaned for magic stringt")
    parser.add_argument("magic_string", help="The text that will be searched")
    parser.add_argument(
        "--polling_interva", "-p", default=.1,
            help="How many times program refreshes in seconds. Default is .2")
    parser.add_argument(
        "--file_extension", "-e", default=".txt",
            help="File extension of file to search. Default is .txt")

    return parser


def signal_handler(sig_num, frame):
    global exit_flag

    # logger.warn('Received ' + signal.signal(sig_num).name)
    exit_flag = True
    logger.warning("QUIT")
    return None


def main(args):
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    if not os.path.exists(parsed_args.directory):
        os.mkdir(parsed_args.directory)

    while not exit_flag:
        logger.debug(parsed_args.magic_string)
        time.sleep(float(parsed_args.polling_interva))
        try:
            # call my directory watching function
            pass
        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            print(e)
            pass

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%

        # time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start


if __name__ == '__main__':
    main(sys.argv[1:])


    # ---------------------
    # 1. Write all doc strings!
    # 2. gitignor file?
    # ---------------------