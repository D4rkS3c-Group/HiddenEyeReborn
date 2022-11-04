import logging
from subprocess import Popen, PIPE, DEVNULL


def check_dependency(name: str, command: str = 'which'):
    try:
        dependency_state = Popen([f"{command}", f"{name}"], stdout=PIPE, stderr=DEVNULL).communicate()[0].decode('utf-8')
    except ValueError():
        dependency_state = None

    return True if name in dependency_state else False
