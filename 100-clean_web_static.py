#!/usr/bin/python3
"""
    Deletes out of date archives
"""

import os
from fabric.api import *

env.hosts = ['54.237.92.226', '3.94.213.63']
env.user = 'ubuntu'
env.identinty = '~/.ssh/school'


def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]