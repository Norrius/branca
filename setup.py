# -*- coding: utf-8 -*-

import os

from setuptools import setup

import versioneer

rootpath = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return open(os.path.join(rootpath, *parts), 'r').read()


def walk_subpkg(name):
    data_files = []
    package_dir = 'branca'
    for parent, dirs, files in os.walk(os.path.join(package_dir, name)):
        # Remove package_dir from the path.
        sub_dir = os.sep.join(parent.split(os.sep)[1:])
        for f in files:
            data_files.append(os.path.join(sub_dir, f))
    return data_files


pkg_data = {'': ['*.js',
                 'plugins/*.js',
                 'plugins/*.html',
                 'plugins/*.css',
                 'plugins/*.tpl',
                 'templates/*.html',
                 'templates/*.js',
                 'templates/*.txt']}
pkgs = ['branca', ]

LICENSE = read('LICENSE.txt')
long_description = '{}\n{}'.format(read('README.rst'), read('CHANGES.txt'))

# Dependencies.
with open('requirements.txt') as f:
    tests_require = f.readlines()
install_requires = [t.strip() for t in tests_require]


setup(
    name='branca',
    version=versioneer.get_version(),
    description='Generate complex HTML+JS pages with Python',
    long_description=long_description,
    author='Martin Journois',
    url='https://github.com/python-visualization/branca',
    keywords='data visualization',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable'
    ],
    packages=pkgs,
    package_data=pkg_data,
    include_package_data=True,
    cmdclass=versioneer.get_cmdclass(),
    tests_require=['pytest'],
    license=LICENSE,
    install_requires=install_requires,
    zip_safe=False,
)
