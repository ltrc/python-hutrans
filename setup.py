#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import warnings
from setuptools import setup, Extension
from Cython.Distutils import build_ext

dist_dir = os.path.dirname(os.path.abspath(__file__))
os.system("gunzip -kf %s/hutrans/models/* 2> /dev/null" %dist_dir)

try:
    import py2exe
except ImportError:
    if len(sys.argv) >= 2 and sys.argv[1] == 'py2exe':
        print("Cannot import py2exe", file=sys.stderr)
        exit(1)

py2exe_options = {
    "bundle_files": 1,
    "compressed": 1,
    "optimize": 2,
    "dist_dir": '.',
    "dll_excludes": ['w9xpopen.exe'],
}

py2exe_console = [{
    "script": "./hutrans/__main__.py",
    "dest_base": "hutrans",
}]

py2exe_params = {
    'console': py2exe_console,
    'options': {"py2exe": py2exe_options},
    'zipfile': None
}

if len(sys.argv) >= 2 and sys.argv[1] == 'py2exe':
    params = py2exe_params
else:
    files_spec = [
        ('share/doc/hutrans', ['README.rst'])
    ]
    root = os.path.dirname(os.path.abspath(__file__))
    data_files = []
    for dirname, files in files_spec:
        resfiles = []
        for fn in files:
            if not os.path.exists(fn):
                warnings.warn('Skipping file %s since it is not present. Type  make  to build all automatically generated files.' % fn)
            else:
                resfiles.append(fn)
        data_files.append((dirname, resfiles))

    params = {
        'data_files': data_files,
    }
    params['entry_points'] = {'console_scripts': ['hutrans = hutrans:main']}

# Get the version from youtube_dl/version.py without importing the package
exec(compile(open('hutrans/version.py').read(),
             'hutrans/version.py', 'exec'))

setup(
    name = "hutrans",
    version = __version__,
    description="Transliteration Tool: Hindi to Urdu transliterator and vice-versa",
    long_description = open('README.rst', 'rb').read().decode('utf8'),
    keywords = ['Language Transliteration', 'Computational Linguistics', 
		'Indic', 'Hindi', 'Urdu', 'Devnagari', 'Persio-Arabic'],
    author=['Riyaz Ahmad', 'Irshad Ahmad'],
    author_email='irshad.bhat@research.iiit.ac.in',
    maintainer='Irshad Ahmad',
    maintainer_email='irshad.bhat@research.iiit.ac.in',
    license = "MIT",
    url="https://github.com/irshadbhat/hutrans",
    package_dir={"hutrams":"hutrans"},
    packages=['hutrans'],
    package_data={'hutrans': ['models/*.npy', 'mapping/*']},

    classifiers=[
        "Topic :: Indian Languages :: Language Identification",
        "Environment :: Console",
        "License :: Public Domain",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension("hutrans.viterbi", ["hutrans/viterbi.pyx"]),
    ],
    install_requires=["cython", "numpy", "scipy"],
    #requires=["cython", "numpy", "scipy"],
    **params
)
