import logging
from urllib.error import HTTPError, URLError
import urllib.request

def verify_connection(url: str = "https://google.com", timeout: float = 10.0) -> bool:
    """Used to verify internet connection.
    
    Args:
        url (str): Specify custom url to ping
        timeout (float): Specify verification timeout
    Returns:
        bool: True if connection is available, False otherwise.
    """
    try:
        url_code = urllib.request.urlopen(url=url, timeout=timeout).getcode()
        if url_code == 200:
            logging.info(f"Successfully connected to {url} - network verified!")
            return True
        else:
            logging.error(f"Failed to connect to {url}. Unexpected status code: {url_code}")
            return False
    except (HTTPError, URLError) as error:
        logging.warning(f'Unable to establish connection with {url}. Error: {error}')
        return False