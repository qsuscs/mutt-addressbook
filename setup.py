from setuptools import setup, find_packages
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mutt-addressbook",
    version="1.1.0",

    scripts=['mutt-addressbook.py'],

    install_requires=['ldap3>=2.1.1'],

    author="Thomas Schneider",
    author_email="qsx+pypi@qsx.re",
    description="An addressbook query for mutt",
    long_description=long_description,
    license="ISC",
    keywords="mutt ldap addressbook address book",
    url="https://github.com/qsuscs/mutt-addressbook",

    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
