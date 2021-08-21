#!/usr/bin/env python
from app_logging.default_logging import logging, log, set_logging_config
from network.verification import verify_connection
from rich.traceback import install


import argparse


LOGGING_LEVEL = logging.DEBUG

def initialize_app():
    install(show_locals=True, width=148)
    parser = argparse.ArgumentParser()
    parser.parse_args()


def main():
    print("Hey, if you can - contact that lazy developer and make him code! Would be glad if you contribute, as well...")
    set_logging_config(level=LOGGING_LEVEL)
    log.info("Success, you can access this via terminal!")
    log.debug("Logging level set to %s", LOGGING_LEVEL)
    verify_connection()


if __name__ == "__main__":
    initialize_app()
    main()