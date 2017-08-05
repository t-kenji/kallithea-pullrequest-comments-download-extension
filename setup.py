# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


__version__='0.0.1'

extra = {}

try:
    from distutils.command.build import build as _build

    class build(_build):
        sub_commands = [('compile_catalog', None)] + _build.sub_commands

    extra['cmdclass'] = {
        'build': build,
    }
except:
    pass

setup(
    name='KallitheaPullrequestCommentsDownload',
    version=__version__,
    description='Pullrequest comments download extension for Kallithea',
    author='t-kenji <protect.2501@gmail.com>',
    license='MIT',

    install_requires=[
        'Kallithea',
    ],

    packages=find_packages(),
    package_data = {
        'kalprcommentsdl': [
            'i18n/*/LC_MESSAGES/*.mo',
        ],
    },
    entry_points={
        'kallithea.extensions': [
            'kalprcommentsdl.pullrequests = kalprcommentsdl.pullrequests',
        ],
    },

    **extra
)
