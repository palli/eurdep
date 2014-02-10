# setup.py ###
#from distutils.core import setup
from setuptools import find_packages, setup
import os

from eurdep import get_version

NAME = "eurdep"
VERSION = get_version()
SHORT_DESC = "Parser for Eurdep messages, which are used for measuring gamma radiation"
LONG_DESC = """ """

datafiles = []

datadirs = []

for i in datadirs:
    for cur_dir, dirlist, filelist in os.walk(i):
        datafiles.append(("/" + cur_dir, filelist))



if __name__ == "__main__":
    manpath = "share/man/man1/"
    etcpath = "/etc/%s" % NAME
    etcmodpath = "/etc/%s/modules" % NAME
    initpath = "/etc/init.d/"
    logpath = "/var/log/%s/" % NAME
    varpath = "/var/lib/%s/" % NAME
    rotpath = "/etc/logrotate.d"
    datarootdir = "/usr/share/%s" % NAME
    setup(
        name='%s' % NAME,
        version=VERSION,
        author='Pall Sigurdsson',
        description=SHORT_DESC,
        long_description=LONG_DESC,
        author_email='palli@opensource.is',
        url='http://github.com/palli/eurdep',
        license='GPL',
        scripts=[],
        packages=find_packages(),
        requires=[],
        #data_files=datafiles,
    )
