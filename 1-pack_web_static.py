#!/usr/bin/python3
""" Fabric script that generates from a content into a .tgz archive """
from fabric.api import local
from time import strftime


def do_pack():
    """
    Generates a .tgz archive
    """
    local("mkdir -p versions")
    timef = strftime("%Y%m%d%H%M%S")
    pack = local("tar -cvzf versions/web_static_{}.tgz web_static/"
                 .format(timef))
    if pack.failed:
        return None
    return pack
