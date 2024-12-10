# -*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='tstl',
    version='1.2.39',
    description='Template scripting testing language (TSTL)',
    long_description_content_type="text/markdown",    
    long_description=open('README.md').read(),
    packages=['tstl'],
    include_package_data=True,
    package_data={
        'tstl': ['static/boilerplate', 'static/boilerplate_cov'],
    },
    license='MIT',
    entry_points={
        "console_scripts": [
            "tstl = tstl.harnessmaker:main",
            "tstl_rt = tstl.randomtester:main",
            "tstl_replay = tstl.replay:main",
            "tstl_reduce = tstl.reduce:main",
            "tstl_markov = tstl.markov:main",
        ]
    },
    keywords='testing tstl',
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'coverage==4.5.2',
    ],
)
