#!/usr/bin/python3
""" Fabric script that  that distributes an archive to your web servers """
from fabric.api import *
from time import strftime
import os.path
env.hosts = ['34.75.49.102', '35.196.238.0']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        """ Archive path = versions/web_static_20170315003959.tgz """
        filename = archive_path.split("/")[1]
        """ filename = web_static_20170315003959.tgz """
        tmp = '/tmp/' + filename
        """ Upload tmp directory of the web server """
        put(archive_path, tmp)
        file_no_ext = filename.split(".")[0]
        folder = '/data/web_static/releases/' + file_no_ext + '/'
        run("sudo mkdir -p {}".format(folder))
        """ Unpack the archive """
        run('sudo tar -xzf {} -C {}'.format(tmp, folder))
        """ Delete the archive from the web server
         /tmp/web_static_20170315003959.tgz """
        run("sudo rm {}".format(tmp))
        run("sudo mv {}web_static/* {}".format(folder, folder))
        run("sudo rm -rf {}/web_static".format(folder))
        symb = '/data/web_static/current'
        """Delete the symbolic link /data/web_static/current """
        run("sudo rm -rf {}".format(symb))
        """ Create a new symbolic link """
        run("sudo ln -s {} {}".format(folder, symb))
        return True
    except:
        return False
