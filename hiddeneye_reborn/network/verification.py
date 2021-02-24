import urllib


def verify_connection(url: str=None):
    """Used to verify internet connection.

    Args:
        url (str): Specify custom url to ping

    Returns:
        bool: True if connection is available, False otherwise.
    """
    verification_url = url if not None else "https://google.com"
    return True if urllib.request.urlopen(url=verification_url).getcode() == 200 else False
