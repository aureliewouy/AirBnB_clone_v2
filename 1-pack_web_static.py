#!/usr/bin/python3
""" Fabric script that generates from a content into a .tgz archive """
from fabric.api import *
from datetime import datetime
import os.path
env.hosts = ['34.75.49.102', '35.196.238.0']
env.user = 'ubuntu'
env.password = '~/.ssh/id_rsa'


def do_pack():
    """
    Generates a .tgz archive
    """
    if not os.path.isdir("versions"):
        local("mkdir -p versions")
    timef = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timef)
    pack = local("tar -cvzf {} web_static"
                 .format(filename))
    if pack.failed:
        return None
    return filename
