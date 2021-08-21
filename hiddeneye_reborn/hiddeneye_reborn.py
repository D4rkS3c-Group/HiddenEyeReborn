#!/usr/bin/env python
from app_logging.default_logging import logging, log, set_logging_config
from network.verification import verify_connection


import argparse


LOGGING_LEVEL = logging.DEBUG

def initialize_app():
    parser = argparse.ArgumentParser()
    parser.parse_args()


def main():
    print("Success, you can access this via terminal!")
    print("Hey, if you can - contact that lazy developer and make him code! Would be glad if you contribute, as well...")
    set_logging_config(level=LOGGING_LEVEL)
    log.debug("Logging level set to %s", LOGGING_LEVEL)
    verify_connection()


if __name__ == "__main__":
    initialize_arguments()
    main()
