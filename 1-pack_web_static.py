#!/usr/bin/python3
'''
    Task 1
'''
from fabric.api import local
import time


def do_pack():
    """Make a tar.gz archive of web_static """

    t = time.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static/".format(t))
    pth = "versions/web_static_{}.tgz".format(t)
    return pth
