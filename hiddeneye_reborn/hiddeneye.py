#!/usr/bin/env python

SUCCESS_MESSAGE = "Success, you can access this via terminal!"
WARNING_MESSAGE = "THIS IS NOT PRODUCTION READY, STOP MAKING USELESS ISSUES PLEASE"


def initialize_app():
    print("App initialized")


def configure_and_log_app():
    print(SUCCESS_MESSAGE)
    print(WARNING_MESSAGE)


def run_app():
    initialize_app()
    configure_and_log_app()
    print("The app is running...")


if __name__ == "__main__":
    run_app()