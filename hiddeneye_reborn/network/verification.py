"""Network verification module"""

from urllib.error import HTTPError, URLError
import urllib.request
import logging


def verify_connection(url: str=None, timeout: float=None):
    """Used to verify internet connection.

    Args:
        url (str): Specify custom url to ping
        timeout (float): Specify verification timeout
    Returns:
        bool: True if connection is available, False otherwise.
    """
    verification_url = url if url is not None else str("https://google.com")
    verification_timeout = timeout if timeout is not None else 10
    try:
        url_code = urllib.request.urlopen(url=verification_url, timeout=float(verification_timeout)).getcode()
        logging.info('Connected, checking code...')
        if url_code == 200:
            logging.info("Verified successfully!")
            return True
    except(HTTPError, URLError) as error:
        logging.warning('Unable to verify connection with %s due to %s, returning False', verification_url, error)
        return False
    
