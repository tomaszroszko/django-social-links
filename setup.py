#! /usr/bin/env python
from distutils.core import setup
import sys
reload(sys).setdefaultencoding('Utf-8')


setup(
    name='django-social-links',
    version='0.0.1',
    author='Tomasz Roszko',
    author_email='tomaszroszko@gmail.com',
    description='Allow to manage social links on the web',
    long_description=open('README.rst').read(),
    url='https://github.com/tomaszroszko/django-social-links',
    license='BSD License',
    platforms=['OS Independent'],
    packages=['sociallinks', 'sociallinks.migrations'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 0.0.1 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
        ],
    )