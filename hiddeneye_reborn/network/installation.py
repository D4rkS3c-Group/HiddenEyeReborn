import logging
from subprocess import Popen, PIPE, DEVNULL


def is_dependency_installed(name: str, command: str = 'which'):
    try:
        command_output = Popen([command, name], stdout=PIPE, stderr=DEVNULL).communicate()[0]
        dependency_path = command_output.decode('utf-8')
    except ValueError:
        dependency_path = ""

    return name in dependency_path