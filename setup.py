import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "SysCompromisos",
    version = "0.1.0",
    url = '',
    license = 'GPL V. 3',
    description = "Compromisos Presidenciales",
    long_description = read('README'),

    author = 'Herald Olivares, Andres Herrada',
    author_email = 'heraldmatias.oz@gmail.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Dev',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Political',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
