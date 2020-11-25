#!/usr/bin/env python3

from setuptools import setup, find_packages
from setuptools.extension import Extension

from Cython.Build import cythonize

from pyv4l2 import __version__


extension_name = 'pyx'
extensions = [
    Extension(
        'pyv4l2.frame',
        ["pyv4l2/frame.%s" % extension_name],
        libraries=["v4l2", ]
    ),
    Extension(
        'pyv4l2.control',
        ["pyv4l2/control.%s" % extension_name],
        libraries=["v4l2", ]
    )
]

extensions = cythonize(extensions)

setup(
    name='pyv4l2',
    version=__version__,
    description='Simple v4l2 for pyv4l2',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Cython',
        'Programming Language :: C',
        'Topic :: Software Development :: Libraries'
    ],
    author='duanhongyi',
    author_email='duanhongyi@doopai.com',
    url='https://github.com/duanhongyi/pyv4l2',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    setup_requires=['Cython>=0.18'],
    extras_require={
        'examples': ['pillow', 'numpy'],
    },
    packages=find_packages(),
    ext_modules=extensions,
)
