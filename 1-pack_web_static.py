#!/usr/bin/python3
'''
    Task 1
'''
from fabric.api import local
import time


def do_pack():
    """Make a tar.gz archive of web_static """
    o = local("mkdir versions; tar -cvzf versi" +
              "ons/web_static_{}.tgz web_static/"
              .format(time.strftime("%Y%m%d%H%M%S")))
