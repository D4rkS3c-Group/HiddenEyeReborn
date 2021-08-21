import logging.config
from rich.logging import RichHandler

def set_logging_config(level: int = None, filename: str = "default.log"):
    logging_level = logging.NOTSET
    if level == 10:
        logging_level = logging.DEBUG
    elif level == 20:
        logging_level = logging.INFO
    elif level == 30:
        logging_level = logging.WARNING
    elif level == 40:
        logging_level = logging.ERROR
    elif level == 50:
        logging_level = logging.CRITICAL
    else:
        logging_level = logging.NOTSET

    logging.basicConfig(level=logging_level,
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        handlers=[
                            logging.FileHandler(filename),
                            RichHandler(show_time=False, show_level=False, omit_repeated_times=False, rich_tracebacks=True)
                        ]
)

log = logging.getLogger(__name__)
