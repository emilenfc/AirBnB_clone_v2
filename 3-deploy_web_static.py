#!/usr/bin/python3
"""Write a Fabric script (based on the file 2-do_deploy_web_static"""

from fabric.api import local, settings, abort, run, cd, env, put, get
from fabric.decorators import task, hosts, with_settings
from os import path
from datetime import datetime


env.hosts = ["54.237.86.111", "52.72.23.83"]
env.user = "ubuntu"
