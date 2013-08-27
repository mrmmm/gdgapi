# -*- coding: utf_8 -*-
__author__ = 'mohammadalmeer'
from datetime import datetime
from fabric.api import local, cd, run, env

env.user = "ubuntu"
#env.hosts = ['ec2-54-227-34-52.compute-1.amazonaws.com']
env.hosts = ['107.21.234.130']
env.key_filename = "/Users/mohammadalmeer/.ssh/mrmmm.pem"
env.forward_agent = True

def mac_deploy(commit_message=None):
    '''Automated deploy from macbook'''
    if not commit_message:
        commit_message = "Automated commit/deploy using Fabric on  %s" % datetime.now().strftime("%Y-%m-%d  %H:%M")
    local("git add .")
    local('git commit -m "%s"' % commit_message)
    local("git push")

def to_ec2():
    code_dir = "/ebs/gdgapi/gdgapi"
    with cd(code_dir):
        run("git pull")
        run("sudo apachectl restart")

def boom(commit_message=None):
    mac_deploy(commit_message)
    to_ec2()