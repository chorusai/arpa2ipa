import os

from setuptools import setup, find_packages
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='brave',

    version='0.1.0rc1',

    description='ARPA2IPA',
    long_description=long_description,

    url='https://github.com/chorusai/arpa2ipa',

    author='Chorus',

    license='Apache Software License',

    classifiers=[

        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='ARPAbet-to-IPA converter',
    packages=find_packages(exclude=[]),
    install_requires=[],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    data_files=
    [
    ]
    ,

    entry_points={
        'console_scripts': [
        ],
    },
)
