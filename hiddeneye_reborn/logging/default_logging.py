import logging

def set_logging_config(level: str = None, filename: str = None):
    logging_level = logging.NOTSET
    if "DEBUG" in level.upper():
        logging_level = logging.DEBUG
    elif "INFO" in level.upper():
        logging_level = logging.INFO
    elif "WARNING" in level.upper():
        logging_level = logging.WARNING
    elif "ERROR" in level.upper():
        logging_level = logging.ERROR
    elif "CRITICAL" in level.upper():
        logging_level = logging.CRITICAL
    else:
        logging_level = logging.NOTSET

    if filename is not None:
        log_file = filename
    else:
        log_file = "default.log"

    logging.basicConfig(level=logging_level,
                        format="[%(levelname)s] %(message)s %(asctime)s",
                        handlers=[
                            logging.FileHandler(filename=log_file),
                            logging.StreamHandler()
                        ]
)
