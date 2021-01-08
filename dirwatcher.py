#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""
import argparse
import datetime
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
    directory_model = {}
    
    for director in os.listdir(path):
        if os.path.isfile(os.path.join(os.path.abspath(path), director)):
            directory_model [director] = 1

    print(directory_model)
    return

# def scan_single_file():
# def detect_added_files():
# def detect_removed_files():

def create_parser():
    """Creates parsing arguments."""

    parser = argparse.ArgumentParser(
        description="Searches a given directory for a specific line of text")
    parser.add_argument(
        "directory", help="The directory that will be scaned for magic stringt")
    parser.add_argument("magic_string", help="The text that will be searched")
    parser.add_argument(
        "--polling_interva", "-p", default=1,
            help="How many times program refreshes in seconds. Default is 1")
    parser.add_argument(
        "--file_extension", "-e", default=".txt",
            help="File extension of file to search. Default is .txt")

    return parser


def signal_handler(sig_num, frame):
    global exit_flag
    # logger.warn('Received ' + signal.Signals(sig_num).name)
    # logger.warn('Received ' + signal.signal(sig_num).name)
    logger.warning(sig_num)

    exit_flag = True
    # logger.warning("QUIT")
    return None


def main(args):
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    start_time = datetime.datetime.now()
    logger.info(
        "\n" +
        "-" * 105 +
        f"\n\tRunning {__file__}" +
        f"\n\tStarted on {start_time.isoformat()}\n" +
        "-" * 105
    )

    if not os.path.exists(parsed_args.directory):
        os.mkdir(parsed_args.directory)

    while not exit_flag:
        try:
            watch_directory(parsed_args.directory, 
                parsed_args.magic_string, parsed_args.file_extension,
                    parsed_args.polling_interva)
            pass
        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            print(e)
            pass
        
        time.sleep(float(parsed_args.polling_interva))

    up_time = datetime.datetime.now() - start_time
    logger.info(
        "\n" +
        "-" * 105 +
        f"\n\tStop {__file__}" +
        f"\n\tUp time was {up_time}\n" +
        "-" * 105
    )


if __name__ == '__main__':
    main(sys.argv[1:])


    # ---------------------
    # 1. Write all doc strings!
    # 2. gitignor file?
    # 3. PEP8
    # ---------------------