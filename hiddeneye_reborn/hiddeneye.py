#!/usr/bin/env python
from hiddeneye_reborn.logs.default_logging import logging, log, set_logging_config
from hiddeneye_reborn.core.text_interface.main import args
from hiddeneye_reborn.network.verification import verify_connection
from rich.traceback import install

LOGGING_LEVEL = logging.DEBUG


def initialize_app():
    install(show_locals=True, width=148)


def main():
    set_logging_config(level=LOGGING_LEVEL)
    log.info("Success, you can access this via terminal!")
    log.info("THIS IS NOT PRODUCTION READY, STOP MAKING USELESS ISSUES PLEASE")
    log.debug("Logging level set to %s", LOGGING_LEVEL)
    verify_connection()
    log.debug("Non-interactive mode set to %s", args.non_interactive)


def execute():
    initialize_app()
    main()

