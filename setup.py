
#! By HookSander

from setuptools import setup

APP = ['script.py']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app' : OPTIONS},
    setup_requires=['py2app']
)