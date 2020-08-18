#!/usr/bin/python3
'''
    Task 3
'''
from fabric.api import local, put, get, sudo, env, run, reboot
import time
import os


env.hosts = ['34.73.244.83', '35.175.186.218']


def do_deploy(archive_path):
    """ deploy archive given as input to /tmp on both web servers """
    if os.path.exists(archive_path):
        put(archive_path, "/tmp/")
    else:
        return False
    plist = archive_path.split('/')
    arch_name = plist[-1]
    wo_ext = arch_name[:-4]
    print(arch_name)
    print(wo_ext)

    run("mkdir -p /data/web_static/releases/{}".format(wo_ext))
    run("tar -xzf /tmp/{} -C /data/".format(arch_name) +
        "web_static/releases/{}/".format(wo_ext))
    run("rm /tmp/{}".format(arch_name))
    run("mv /data/web_static/releases/{}/".format(wo_ext) +
        "web_static/* /data/web_static/releases/{}/".format(wo_ext))
    run("rm -rf /data/web_static/releases/{}/web_static".format(wo_ext))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ ".format(wo_ext) +
        "/data/web_static/current")
    return True


def do_pack():
    """Make a tar.gz archive of web_static """

    t = time.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static/".format(t))
    pth = "versions/web_static_{}.tgz".format(t)
    return pth


def deploy():
    """ deploy using do_pack and do_deploy """
    p = do_pack()
    if p is None:
        return False
    d = do_deploy(p)
    return d
