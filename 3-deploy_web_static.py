#!/usr/bin/python3
'''
    Task 3
'''
from fabric.api import local, put, get, sudo, env, run, reboot
import time
import os


do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack
env.hosts = ['34.73.244.83', '35.175.186.218']


def deploy():
    """ deploy using do_pack and do_deploy """
    p = do_pack()
    if p is None:
        return False
    d = do_deploy(p)
    return d
