#!/usr/bin/env python
from .logs.default_logging import logging, log, configure_logging
from .core.text_interface.main import args
from .network.verification import verify_connection

from rich.traceback import install

LOGGING_LEVEL = logging.DEBUG
SUCCESS_MESSAGE = "Success, you can access this via terminal!"
WARNING_MESSAGE = "THIS IS NOT PRODUCTION READY, STOP MAKING USELESS ISSUES PLEASE"


def initialize_app():
    install(show_locals=True, width=148)


def configure_and_log_app():
    configure_logging(level=LOGGING_LEVEL)
    log_info_multiple_messages([SUCCESS_MESSAGE, WARNING_MESSAGE])
    log.debug("Logging level set to %s", LOGGING_LEVEL)
    verify_connection()
    log.debug("Non-interactive mode set to %s", args.non_interactive)


def log_info_multiple_messages(messages):
    for message in messages:
        log.info(message)


def run_app():
    initialize_app()
    configure_and_log_app()


if __name__ == "__main__":
    run_app()