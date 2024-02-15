import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.theme import Theme

LOG_LEVELS = {
    10: logging.DEBUG,
    20: logging.INFO,
    30: logging.WARNING,
    40: logging.ERROR,
    50: logging.CRITICAL
}

theme = Theme({"DEBUG": "dim cyan", "INFO": "green", "WARNING": "yellow", "ERROR": "red", "CRITICAL": "bold red",})
console = Console(theme=theme)

# Constants
DEFAULT_LOG_FILENAME = "default.log"
LOG_FORMAT = "%(message)s"



def configure_logging(level: int = None, filename: str = DEFAULT_LOG_FILENAME):
    expected_logging_level = LOG_LEVELS.get(level, logging.NOTSET)
    logging.basicConfig(
        level=expected_logging_level,
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(filename),
            RichHandler(
                console=console,
                show_time=True,
                show_level=True,
                omit_repeated_times=False,
                rich_tracebacks=True
            )
        ]
    )

log = logging.getLogger(__name__)
