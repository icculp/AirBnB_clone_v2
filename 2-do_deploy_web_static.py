#!/usr/bin/python3
'''
    Task 2
'''
from fabric.api import local, put, get, sudo, env, run, reboot
import time
import os


env.hosts = ['34.73.244.83', '35.175.186.218']


def do_deploy(archive_path):
    """ deploy archive given as input to /tmp on both web servers """
    if os.path.exists("./" + archive_path):
        put(archive_path, '/tmp/')
        print('true')
    else:
        print('returning false')
        print("./" + archive_path)
        return False
    plist = archive_path.split('/')
    arch_name = plist[-1]
    wo_ext = arch_name[:-4]

    run("mkdir -p /data/web_static/releases/{}".format(wo_ext))
    run("tar -xzf /tmp/{} -C /data/" +
        "web_static/releases/{}/".format(arch_name, wo_ext))
    run("rm /tmp/{}".format(arch_name))
    run("mv /data/web_static/releases/{}/" +
        "web_static/* /data/web_static/releases/{}/".format(wo_ext, wo_ext))
    run("rm -rf /data/web_static/releases/{}/web_static".format(wo_ext))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ " +
        "/data/web_static/current".format(wo_ext))
    return True
